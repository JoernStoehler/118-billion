import markdown
from human import Human

def html_text(human: Human):
    #text = human.vars_html["Obituary"] # markdown
    text = human.vars_html["Biography"]

    # name
    name = human.vars_html["Title Data"]["name"].strip()
    birth_date = human.vars_html["Title Data"]["exact birth date"].strip()
    death_date = human.vars_html["Title Data"]["exact death date"].strip()
    place = human.vars_html["Title Data"]["home area"].strip()

    # insert title
    text = f"**{name}**\n\n{birth_date} - {death_date}\n\n{place}\n\n{text}"

    html = markdown.markdown(text) # html

    with open(human.files.text, "w") as f:
        f.write(html)