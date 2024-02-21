import pytest
from utils.dicts import get_val


@pytest.mark.parametrize('dict_, key_, val, res',
                         [({"vcs": "mercurial"}, "vcs", None, "mercurial"),
                          ({"vcs": "mercurial"}, "vcs", "git", "mercurial"),
                          ({}, "vcs", "git", "git"),
                          ({}, "vcs", "bazaar", "bazaar")])
def test_get_val(dict_, key_, val, res):
    assert get_val(dict_, key_, val) == res
