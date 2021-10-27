from invoke import Collection, task


@task
def clean(ctx):
    """Remove all the tmp files in .gitignore"""
    ctx.run("git clean -Xdf")


@task
def docker(ctx):
    """Build docker image"""
    ctx.run("pipenv lock --keep-outdated --requirements > requirements.txt")
    user_name = "pycontw"
    proj_name = "python_project"
    repo_name = f"{user_name}/{proj_name}"
    ctx.run(f"docker build -t {repo_name}:latest .")


build_ns = Collection("build")
build_ns.add_task(clean)
build_ns.add_task(docker)
