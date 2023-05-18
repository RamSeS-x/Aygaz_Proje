# github_connection.py

from github import Github
def connect_to_github():
    # GitHub bağlantı kodunu burada tanımlayın
    token = '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'
    g = Github(token)
    repo = g.get_repo('RamSeS-x/Aygaz_proje')
    return repo
# github_connection.py



