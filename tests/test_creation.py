import os
import pytest
from subprocess import check_output
from conftest import system_check


def no_curlies(filepath):
    """ Utility to make sure no curly braces appear in a file.
        That is, was Jinja able to render everything?
    """
    with open(filepath, 'r') as f:
        data = f.read()

    template_strings = [
        '{{',
        '}}',
        '{%',
        '%}'
    ]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)


@pytest.mark.usefixtures("default_baked_project")
class TestCookieSetup(object):
    def test_project_name(self):
        project = self.path
        assert project.name == 'project_name'

    def test_author(self):
        setup_ = self.path / 'setup.py'
        args = ['python', str(setup_), '--author']
        p = check_output(args).decode('ascii').strip()
        if pytest.param.get('author_name'):
            assert p == 'author_name'
        else:
            assert p == 'Your name (or your organization/company/team)'
    
    def test_author_email(self):
        setup_ = self.path / 'setup.py'
        args = ['python', str(setup_), '--author-email']
        p = check_output(args).decode('ascii').strip()
        print(p)
        if pytest.param.get('author_email'):
            assert p == 'author_email'
        else:
            assert p == 'Your email (or your organization/company/team email)'

    def test_readme(self):
        readme_path = self.path / 'README.md'
        assert readme_path.exists()
        assert no_curlies(readme_path)
        if pytest.param.get('project_name'):
            with open(readme_path) as fin:
                assert 'project_name' == next(fin).strip()

    def test_setup(self):
        setup_ = self.path / 'setup.py'
        args = ['python', str(setup_), '--version']
        p = check_output(args).decode('ascii').strip()
        assert p == '0.0.1'

    def test_license(self):
        license_path = self.path / 'LICENSE'
        assert license_path.exists()
        assert no_curlies(license_path)

    def test_license_type(self):
        setup_ = self.path / 'setup.py'
        args = ['python', str(setup_), '--license']
        p = check_output(args).decode('ascii').strip()
        if pytest.param.get('open_source_license'):
            assert p == 'BSD-3'
        else:
            assert p == 'MIT'


    def test_folders(self):
        expected_dirs = [
            'data',
            'data/external',
            'data/interim',
            'data/processed',
            'data/raw',
            'docs',
            'models',
            'models/model_outputs',
            'notebooks',
            'references',
            'reports',
            'reports/figures',
            'tests',
            'src',
            'src/common',
            'src/data',
            'src/features',
            'src/model_evaluation',
            'src/modelling',
            'src/reporting',
            'src/visualization',
        ]

        ignored_dirs = [
            str(self.path)
        ]

        abs_expected_dirs = [str(self.path / d) for d in expected_dirs]
        abs_dirs, _, _ = list(zip(*os.walk(self.path)))
        assert len(set(abs_expected_dirs + ignored_dirs) - set(abs_dirs)) == 0

