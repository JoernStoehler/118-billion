from human import Human

def make_human(id: str):
    human = Human(id)

    ## SAMPLE VARIABLES
    # Edit here to change the statistical variables used
    # Earlier defined variables are available to the LLM and will be conditioned on

    from sample_birth_year import sample_birth_year
    from sample_llm import sample_llm
    from sample_random import sample_random

    sample_birth_year(human, "Birth Year")
    sample_llm(human, "Birth Region")
    sample_llm(human, "Birth Subregion")
    sample_llm(human, "Ethnicity")
    sample_llm(human, "Parents Socioeconomic Class")
    sample_random(human, "Gender", {"male": 0.5, "female": 0.5})
    sample_llm(human, "Age at Death")
    sample_llm(human, "Cause of Death")
    sample_llm(human, "Occupation")
    sample_llm(human, "Religion")
    sample_llm(human, "Marital Status")
    sample_llm(human, "Family Structure")

    ## GENERATE HTML
    # Edit here to change how the html pages are generated

    from html_llm_biography import html_llm_biography
    from html_llm_image import html_llm_image
    from html_text import html_text

    html_llm_biography(human)
    html_llm_image(human)
    html_text(human)

    ## PUT INTO LIST
    datalist = open("docs/data.csv", "r").read().split("\n")
    datalist = datalist + [id]
    datalist = sorted(set(datalist))
    datalist = "\n".join(datalist)
    with open("docs/data.csv", "w") as f:
        f.write(datalist)

def get_all_ids():
    # find all ids in docs/data/*.png
    import glob
    import os
    ids = [os.path.basename(f).split(".")[0] for f in glob.glob("docs/data/*.json")]
    return ids

if __name__ == "__main__":
    import argparse
    import uuid
    import os

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--id", type=str, default=None, help="make/finish a human with the given id")
    group.add_argument("--finish", action="store_true", help="finish all humans")
    group.add_argument("--new", action="store_true", help="make a new human")
    args = parser.parse_args()

    if args.id is not None or args.new:
        id = args.id if args.id is not None else str(uuid.uuid4())

        print(f"docs/data/{id}.json")
        print(f"logs/{id}.log")
        import logging
        file_log = os.path.join("logs", f"{id}.log")
        logging.basicConfig(level=logging.INFO, filename=file_log, filemode="a", format="%(asctime)s %(levelname)s %(message)s", force=True)

        make_human(id)
    elif args.finish:
        ids = get_all_ids()
        for id in ids:
            print(f"docs/data/{id}.json")
            print(f"logs/{id}.log")
            import logging
            file_log = os.path.join("logs", f"{id}.log")
            logging.basicConfig(level=logging.INFO, filename=file_log, filemode="a", format="%(asctime)s %(levelname)s %(message)s", force=True)

            make_human(id)