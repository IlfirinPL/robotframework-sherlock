from pathlib import Path

from .. import Tree, Keyword, AcceptanceTest


class TestResolveVariables(AcceptanceTest):
    ROOT = Path(Path(__file__).parent, "test_data")

    def test(self):
        data = self.run_sherlock()
        expected = Tree(
            name="test_data",
            children=[
                Tree(name="Library1", keywords=[Keyword(name="Keyword 1", used=1)]),
                Tree(name="Library2.py", keywords=[]),
                Tree(name="test.robot", keywords=[]),
            ],
        )
        self.should_match_tree(expected, data)
