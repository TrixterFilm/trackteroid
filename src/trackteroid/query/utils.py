#  BSD 3-Clause License
#
#  Copyright (c) 2023, Trixter GmbH
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#  3. Neither the name of the copyright holder nor the names of its
#     contributors may be used to endorse or promote products derived from
#     this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#  OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

# TODO: Move this into query.py
def build_partial_query(target, arguments, attribute):
    """

    Args:
        target (TargetRelation): target relation data (relation + collection).
        arguments (tuple): attribute values/patterns to match in the query.
        attribute (str): attribute chain.

    Returns:
        str: partial query expression.

    """
    def _build_for_relation(relation, attribute):
        pattern_match_expressions = []
        non_pattern_elements = []
        for element in arguments:
            if isinstance(element, str) and "%" in element:
                pattern_match_expressions.append(
                        "{} like \"{}\"".format(attribute, element)
                )
            else:
                non_pattern_elements.append("\"{}\"".format(element))

        non_pattern_expressions = []

        # handle known id shortcuts like parent.id -> parent_id, version.id -> version_id
        if attribute == "id" and target.relation and not target.collection:
            relation_tokens = relation.split(".")
            if len(relation_tokens) > 1:
                attribute = "{}_id".format(relation_tokens[-1])
                relation = ".".join(relation_tokens[:-1])
            else:
                attribute = "{}_id".format(relation_tokens[0])
                relation = ""

        if len(non_pattern_elements) == 1:
            non_pattern_expressions.append(
                "{} is {}".format(attribute, non_pattern_elements[0])
            )
        elif non_pattern_elements:
            non_pattern_expressions.append(
                "{} in ({})".format(attribute, ",".join(non_pattern_elements))
            )

        # Attribute expression
        query = "({})".format(" or ".join(non_pattern_expressions + pattern_match_expressions))

        if relation:
            # Relation expression
            query = "{} {} {}".format(relation, "any" if target.collection else "has", query)

        return query

    relations = [target.relation] if not isinstance(target.relation, list) else target.relation
    if len(relations) > 1:
        start, end = "(", ")"
    else:
        start, end = "", ""

    return start + " or ".join(_build_for_relation(relation, attribute) for relation in relations) + end
