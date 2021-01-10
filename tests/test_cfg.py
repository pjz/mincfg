
import os

from mincfg import MergedConfiguration, DictSource, OSEnvironSource





def test_merged_case_insensitive():

    d1 = {
        'a': '11', 
        'B': '12',
        'C': { 
            'Ca': '131', 
            'CB': '132'
        }
    }

    d2 = {
        'A': '21',
        'c': {
            'ca': '231',
            'cc': '233'
        },
        'd': '24',
    }

    config = MergedConfiguration([DictSource(d1), DictSource(d2)])

    assert config.get('a') == '21'
    assert config.get('b') == '12'
    assert config.get('d') == '24'

    for k in ('a', 'b', 'd'):
        assert config.get(k.lower()) == config.get(k.upper())


def test_osenviron_source():

    cur_keys = set(os.environ.keys())
    os.environ.update({
        'MINCFGTST_A': 'a',
        'MINCFGTST_B': 'b',
        'MINCFGTST_C_A': 'ca',
        'MINCFGTST_C_B': 'cb',
    })

    shell = os.environ.get('SHELL', 'no-shell-defined')
    user = os.environ.get('USER', 'unknown user')

    config = MergedConfiguration([OSEnvironSource('MINCFGTST')])
    assert config.get('a') == 'a'
    assert config.get('b') == 'b'
    assert config.get('a', namespace=['c']) == 'ca'
    assert config.get('b', namespace=['c']) == 'cb'

