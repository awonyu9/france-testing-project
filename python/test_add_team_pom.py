from models.add_team import AddTeamPage
from models.list_teams import ListTeamsPage

def test_add_team_pom(page):
    add_team_page = AddTeamPage(page)
    add_team_page.navigate()
    team_name = "my team"
    add_team_page.fill(team_name)
    add_team_page.add()

    list_teams_page = ListTeamsPage(page)
    list_teams_page.navigate()
    
    # Check the new team is there
    assert list_teams_page.is_team_visible(team_name)
