from lark import Lark
def main():
    print("2.0 here we come...")
    rule_parser = Lark(r"""
        %import common.WS
        %import common.CNAME
        %import common.NUMBER
        %ignore WS

        rule: NAME "=" (directory_expression | file_expression | distribution_expression)

        directory_expression: "{" [directory_item ("," directory_item)* ] "}"
        directory_item: ("(" [NAME ("," NAME)* ] ")" | NAME) distribution_invocation?

        file_expression: "(" NAME "(" [NUMBER ("," NUMBER)* ] ")" ")"

        distribution_expression: NAME "(" [NUMBER ("," NUMBER)* ] ")"
        distribution_invocation: "[" distribution_expression "]"

        start: rule*

        NAME: CNAME
    """)