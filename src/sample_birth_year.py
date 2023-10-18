# interpolate population data
import csv
import numpy
import logging
import scipy.interpolate
from typing import Optional, OrderedDict
from human import Human

def get_birth_percentiles(year_start, year_end):
    """
    Enables sampling the year of a random human birth.
    Returns:
        years: numpy array of consecutive years
        percentiles: numpy array of percentiles        
    """

    src_file = "src/sample_birth_year.csv"
    # year, population per 1k, births per 1k
    # -190000, 0.1, 80
    #  -50000, 2, 80
    # ...

    # read data
    with open(src_file, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        src = list(reader)
        src = src[1:] # remove header
        src = [[int(row[0]), float(row[1]), float(row[2])] for row in src]

    src_year = numpy.array([row[0] for row in src]) 
    src_pop = numpy.array([row[1] for row in src]) * 1e6
    src_birth = numpy.array([row[2] for row in src]) * 1e3

    src_bpy = src_pop * src_birth
    src_log_bpy = numpy.log(src_bpy)
    fn_log_bpy = scipy.interpolate.interp1d(src_year, src_log_bpy, kind='linear')

    assert year_start >= src_year[0]
    assert year_end <= src_year[-1]

    year = numpy.arange(year_start, year_end + 1)
    log_bpy = fn_log_bpy(year)
    bpy = numpy.exp(log_bpy)

    bsum = numpy.cumsum(bpy)
    bsum = bsum / bsum[-1]

    return year, bsum

def sample_birth_year(human: Human, var_name: str = "birth_year", year_range = (-190000, 2030)):
    """
    Sample the birth year of a random human.

    :param human: human to sample for
    :param var_name: name of the variable to store the result in
    :param year_range: restrict to births within the given range
    """
    if human.vars_stat.get(var_name) is not None:
        logging.info(f"Variable {var_name} already sampled.")
        return

    tgt_perc = numpy.random.uniform()
    year, perc = get_birth_percentiles(*year_range)
    # find the year that corresponds to the percentile
    tgt_idx = numpy.searchsorted(perc, tgt_perc)
    tgt_year = int(year[tgt_idx])

    value = f"{tgt_year} AD" if tgt_year > 0 else f"{-tgt_year+1} BC"
    logging.info(f"Sampled value: {var_name}={value}")

    # store value
    human.vars_stat[var_name] = value
    human.save()