import yaml
from datetime import timedelta, datetime
from utils import days_to_workhours, workhours_to_days

today = datetime.now().date()

config = {}
with open("./config.yaml") as f:
    config = yaml.load(f, yaml.SafeLoader)

finished_projects = []
not_finished_projects = []
for project in config["projects"]:
    if not project.get("end"):
        not_finished_projects.append(project)
    else:
        if not project.get("start"):
            print("ERROR: Project %s has an end date but no starting date." % project["name"])
            continue
        finished_projects.append(project)

print("-" * 25)
factors = []
last_finish = config["start"]
finished_projects = sorted(finished_projects, key=lambda el: el.get("start"))
for project in finished_projects:
    print("Name\t\t: " + project["name"])
    wasted_time = days_to_workhours((project["start"] - last_finish).days)
    if project["end"] > last_finish:
        last_finish = project["end"]

    pdf_time = project["hours"]

    real_time = days_to_workhours((project["end"] - project["start"]).days)

    total_time = real_time
    total_time += wasted_time
    factor = round(total_time / pdf_time, 3)
    factors.append(factor)
    if (wasted_time):
        print("Wasted Time\t: %3dh" % wasted_time)
    print("Time PDF\t: %3dh" % pdf_time)
    print("Time Real\t: %3dh" % real_time)
    print("Time Total\t: %3dh" % total_time)
    print("Factor\t\t: %7.3f" % factor)
    print("-" * 25)

print("\n")
print("-" * 25)
avg_factor = sum(factors) / len(factors)
print("Avg. Speed Factor: %.3f" % avg_factor)
print("-" * 25)
print("\n")

print("-" * 25)
for project in not_finished_projects:
    print("Name\t\t: " + project["name"])
    pdf_time = project["hours"]
    real_time = round(pdf_time * avg_factor)

    start_date = last_finish
    if project.get("start"):
        start_date = project["start"]
    wasted_time = days_to_workhours((start_date - last_finish).days)
    last_finish = start_date + timedelta(days=workhours_to_days(real_time))
    if (wasted_time):
        print("Wasted Time\t: %3dh" % wasted_time)
    print("Time PDF\t: %3dh" % pdf_time)
    print("Time Real\t: %3dh" % real_time)
    print("Finish Date\t: %s" % datetime.strftime(last_finish, "%Y-%m-%d"))
    if (last_finish <= today):
        print("  !!  FINISH ASAP  !!")
    print("-" * 25)

need_blackhole = (last_finish - today).days
print("Need %d blackhole days" % need_blackhole)
