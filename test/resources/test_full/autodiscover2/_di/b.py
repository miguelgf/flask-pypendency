from pypendency.argument import Argument
from pypendency.builder import ContainerBuilder
from pypendency.definition import Definition


def load(container_builder: ContainerBuilder):
    container_builder.set_definition(
        Definition(
            "test.resources.test_full.autodiscover2.b.B",
            "test.resources.test_full.autodiscover2.b.B",
            [Argument.no_kw_argument("@test.resources.test_full.autodiscover1.a.A")]
        )
    )
