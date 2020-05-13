from libcst.codemod import CodemodTest

from django_codemod.commands.django_40 import (
    ForceTextToForceStrCommand,
    SmartTextToForceStrCommand,
    UGetTextToGetTextCommand,
    UGetTextLazyToGetTextLazyCommand,
    UGetTextNoopToGetTextNoopCommand,
    UNGetTextToNGetTextCommand,
    UNGetTextLazyToNGetTextLazyCommand,
    URLToRePathCommand,
    Django40Command,
)


class TestForceTextToForceStrCommand(CodemodTest):

    TRANSFORM = ForceTextToForceStrCommand

    def test_noop(self) -> None:
        """Test when nothing should change."""
        before = """
            from django import conf
            from django.utils import encoding

            foo = force_str("bar")
        """
        after = """
            from django import conf
            from django.utils import encoding

            foo = force_str("bar")
        """

        self.assertCodemod(before, after)

    def test_simple_substitution(self) -> None:
        """Check simple use case."""
        before = """
            from django.utils.encoding import force_text

            result = force_text(content)
        """
        after = """
            from django.utils.encoding import force_str

            result = force_str(content)
        """
        self.assertCodemod(before, after)

    def test_already_imported_substitution(self) -> None:
        """Test case where force_str is already in the imports."""
        before = """
            from django.utils.encoding import force_text, force_str

            result = force_text(content)
        """
        after = """
            from django.utils.encoding import force_str

            result = force_str(content)
        """
        self.assertCodemod(before, after)

    def test_call_no_value(self) -> None:
        """Regression test for function call without name."""
        before = """
            factory()()
        """
        after = """
            factory()()
        """
        self.assertCodemod(before, after)

    def test_lambda_no_value(self) -> None:
        """Regression test for lambda call without name."""
        before = """
            (lambda x: x)(something)
        """
        after = """
            (lambda x: x)(something)
        """
        self.assertCodemod(before, after)


class TestSmartTextToForceStrCommand(CodemodTest):

    TRANSFORM = SmartTextToForceStrCommand

    def test_noop(self) -> None:
        """Test when nothing should change."""
        before = """
            from django import conf
            from django.utils import encoding

            foo = smart_str("bar")
        """
        after = """
            from django import conf
            from django.utils import encoding

            foo = smart_str("bar")
        """

        self.assertCodemod(before, after)

    def test_simple_substitution(self) -> None:
        """Check simple use case."""
        before = """
            from django.utils.encoding import smart_text

            result = smart_text(content)
        """
        after = """
            from django.utils.encoding import smart_str

            result = smart_str(content)
        """
        self.assertCodemod(before, after)

    def test_already_imported_substitution(self) -> None:
        """Test case where smart_str is already in the imports."""
        before = """
            from django.utils.encoding import smart_text, smart_str

            result = smart_text(content)
        """
        after = """
            from django.utils.encoding import smart_str

            result = smart_str(content)
        """
        self.assertCodemod(before, after)


class TestUGetTextToGetTextCommand(CodemodTest):

    TRANSFORM = UGetTextToGetTextCommand

    def test_noop(self) -> None:
        """Test when nothing should change."""
        before = """
            from django import conf
            from django.utils import translation

            foo = gettext("bar")
        """
        after = """
            from django import conf
            from django.utils import translation

            foo = gettext("bar")
        """

        self.assertCodemod(before, after)

    def test_simple_substitution(self) -> None:
        """Check simple use case."""
        before = """
            from django.utils.translation import ugettext

            result = ugettext(content)
        """
        after = """
            from django.utils.translation import gettext

            result = gettext(content)
        """
        self.assertCodemod(before, after)

    def test_already_imported_substitution(self) -> None:
        """Test case where gettext is already in the imports."""
        before = """
            from django.utils.translation import ugettext, gettext

            result = ugettext(content)
        """
        after = """
            from django.utils.translation import gettext

            result = gettext(content)
        """
        self.assertCodemod(before, after)


class TestUGetTextLazyToGetTextLazyCommand(CodemodTest):

    TRANSFORM = UGetTextLazyToGetTextLazyCommand

    def test_noop(self) -> None:
        """Test when nothing should change."""
        before = """
            from django import conf
            from django.utils import translation

            foo = gettext_lazy("bar")
        """
        after = """
            from django import conf
            from django.utils import translation

            foo = gettext_lazy("bar")
        """

        self.assertCodemod(before, after)

    def test_simple_substitution(self) -> None:
        """Check simple use case."""
        before = """
            from django.utils.translation import ugettext_lazy

            result = ugettext_lazy(content)
        """
        after = """
            from django.utils.translation import gettext_lazy

            result = gettext_lazy(content)
        """
        self.assertCodemod(before, after)

    def test_already_imported_substitution(self) -> None:
        """Test case where gettext_lazy is already in the imports."""
        before = """
            from django.utils.translation import ugettext_lazy, gettext_lazy

            result = ugettext_lazy(content)
        """
        after = """
            from django.utils.translation import gettext_lazy

            result = gettext_lazy(content)
        """
        self.assertCodemod(before, after)


class TestUGetTextNoopToGetTextNoopCommand(CodemodTest):

    TRANSFORM = UGetTextNoopToGetTextNoopCommand

    def test_noop(self) -> None:
        """Test when nothing should change."""
        before = """
            from django import conf
            from django.utils import translation

            foo = gettext_noop("bar")
        """
        after = """
            from django import conf
            from django.utils import translation

            foo = gettext_noop("bar")
        """

        self.assertCodemod(before, after)

    def test_simple_substitution(self) -> None:
        """Check simple use case."""
        before = """
            from django.utils.translation import ugettext_noop

            result = ugettext_noop(content)
        """
        after = """
            from django.utils.translation import gettext_noop

            result = gettext_noop(content)
        """
        self.assertCodemod(before, after)

    def test_already_imported_substitution(self) -> None:
        """Test case where gettext_noop is already in the imports."""
        before = """
            from django.utils.translation import ugettext_noop, gettext_noop

            result = ugettext_noop(content)
        """
        after = """
            from django.utils.translation import gettext_noop

            result = gettext_noop(content)
        """
        self.assertCodemod(before, after)


class TestUNGetTextToNGetTextCommand(CodemodTest):

    TRANSFORM = UNGetTextToNGetTextCommand

    def test_noop(self) -> None:
        """Test when nothing should change."""
        before = """
            from django import conf
            from django.utils import translation

            foo = ngettext("bar", "bars", count)
        """
        after = """
            from django import conf
            from django.utils import translation

            foo = ngettext("bar", "bars", count)
        """

        self.assertCodemod(before, after)

    def test_simple_substitution(self) -> None:
        """Check simple use case."""
        before = """
            from django.utils.translation import ungettext

            result = ungettext(content, plural_content, count)
        """
        after = """
            from django.utils.translation import ngettext

            result = ngettext(content, plural_content, count)
        """
        self.assertCodemod(before, after)

    def test_already_imported_substitution(self) -> None:
        """Test case where ngettext is already in the imports."""
        before = """
            from django.utils.translation import ungettext, ngettext

            result = ungettext(content, plural_content, count)
        """
        after = """
            from django.utils.translation import ngettext

            result = ngettext(content, plural_content, count)
        """
        self.assertCodemod(before, after)


class TestUNGetTextLazyToNGetTextLazyCommand(CodemodTest):

    TRANSFORM = UNGetTextLazyToNGetTextLazyCommand

    def test_noop(self) -> None:
        """Test when nothing should change."""
        before = """
            from django import conf
            from django.utils import translation

            foo = ngettext_lazy("bar", "bars", count)
        """
        after = """
            from django import conf
            from django.utils import translation

            foo = ngettext_lazy("bar", "bars", count)
        """

        self.assertCodemod(before, after)

    def test_simple_substitution(self) -> None:
        """Check simple use case."""
        before = """
            from django.utils.translation import ungettext_lazy

            result = ungettext_lazy(content, plural_content, count)
        """
        after = """
            from django.utils.translation import ngettext_lazy

            result = ngettext_lazy(content, plural_content, count)
        """
        self.assertCodemod(before, after)

    def test_already_imported_substitution(self) -> None:
        """Test case where ngettext_lazy is already in the imports."""
        before = """
            from django.utils.translation import ungettext_lazy, ngettext_lazy

            result = ungettext_lazy(content, plural_content, count)
        """
        after = """
            from django.utils.translation import ngettext_lazy

            result = ngettext_lazy(content, plural_content, count)
        """
        self.assertCodemod(before, after)


class TestURLToRePathCommand(CodemodTest):

    TRANSFORM = URLToRePathCommand

    def test_noop(self) -> None:
        """Test when nothing should change."""
        before = """
            from django.urls import include, re_path

            urlpatterns = [
                re_path(r'^index/$', views.index, name='index'),
                re_path(r'^weblog/', include('blog.urls')),
            ]
        """
        after = """
            from django.urls import include, re_path

            urlpatterns = [
                re_path(r'^index/$', views.index, name='index'),
                re_path(r'^weblog/', include('blog.urls')),
            ]
        """

        self.assertCodemod(before, after)

    def test_simple_substitution(self) -> None:
        """Check simple use case."""
        before = """
            from django.urls import include
            from django.conf.urls import url

            urlpatterns = [
                url(r'^index/$', views.index, name='index'),
                url(r'^weblog/', include('blog.urls')),
            ]
        """
        after = """
            from django.urls import re_path, include

            urlpatterns = [
                re_path(r'^index/$', views.index, name='index'),
                re_path(r'^weblog/', include('blog.urls')),
            ]
        """
        self.assertCodemod(before, after)

    def test_already_imported_substitution(self) -> None:
        """Test case where re_path is already in the imports."""
        before = """
            from django.urls import include, re_path
            from django.conf.urls import url

            urlpatterns = [
                url(r'^index/$', views.index, name='index'),
                re_path(r'^weblog/', include('blog.urls')),
            ]
        """
        after = """
            from django.urls import include, re_path

            urlpatterns = [
                re_path(r'^index/$', views.index, name='index'),
                re_path(r'^weblog/', include('blog.urls')),
            ]
        """
        self.assertCodemod(before, after)


class TestDjango40Command(CodemodTest):

    TRANSFORM = Django40Command

    def test_url_replace_substitution(self) -> None:
        """Check replacement of url()."""
        before = """
            from django.urls import include
            from django.conf.urls import url

            urlpatterns = [
                url(r'^index/$', views.index, name='index'),
                url(r'^weblog/', include('blog.urls')),
            ]
        """
        after = """
            from django.urls import re_path, include

            urlpatterns = [
                re_path(r'^index/$', views.index, name='index'),
                re_path(r'^weblog/', include('blog.urls')),
            ]
        """
        self.assertCodemod(before, after)

    def test_utils_substitution(self) -> None:
        """Check replacement of django.utils."""
        before = """
            from django.utils.encoding import force_text, smart_text
            from django.utils.translation import ugettext, ugettext_lazy

            text1 = force_text(content)
            text2 = smart_text(content)
            trans1 = ugettext(content)
            trans3 = ugettext_lazy(content)
        """
        after = """
            from django.utils.encoding import force_str, smart_str
            from django.utils.translation import gettext, gettext_lazy

            text1 = force_str(content)
            text2 = smart_str(content)
            trans1 = gettext(content)
            trans3 = gettext_lazy(content)
        """
        self.assertCodemod(before, after)
