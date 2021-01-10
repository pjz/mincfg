
import os

from mincfg import MergedConfiguration, DictSource, OSEnvironSource, SubsetSource, YamlFileSource



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


def test_subset_source():

    a = {'a': '1',
         'b': '1',
         'c': '1'
        }
    b = {'a': '2',
         'b': '2',
         'c': '2'
        }
    a_src = DictSource(a)
    b_src = DictSource(b)
    config = MergedConfiguration([a_src, b_src, SubsetSource(a_src, set('a'))])

    assert config.get('a') == '1'
    assert config.get('b') == '2'
    assert config.get('c') == '2'


def test_yaml_file_source(tmp_path):

    # make up a tempfile name
    yamlfile = tmp_path / "config.yaml"

    # write test config to the temp file
    yamlfile.write_text("a: 1\nb: 2\nc:\n  ca: 3\n  cb: 4\n\n")

    # point the config at it
    config = MergedConfiguration([YamlFileSource(str(yamlfile))])

    assert config.get('a') == '1'
    assert config.get('b') == '2'
    assert config.get('ca', namespace=['c']) == '3'
    assert config.get('cb', namespace=['c']) == '4'

