import unittest
from pathlib import Path
from src.domain import load_domain

class DomainTest(unittest.TestCase):
    def test_fixture_matches_domain(self):
        value = load_domain(Path("fixtures/domain.json"))
        self.assertEqual(value["domain"], "public-commitment-progress")
        self.assertGreaterEqual(len(value["constraints"]), 2)

    def test_traceability_chain_documented(self):
        value = load_domain(Path("fixtures/domain.json"))
        facts = "。".join(value["facts"])
        for stage in ["提交人授权", "意见原文", "议题拆分", "相似意见归并",
                      "部门会签", "采纳状态", "政策条款", "公开答复"]:
            self.assertIn(stage, facts)

    def test_handling_rules_documented(self):
        value = load_domain(Path("fixtures/domain.json"))
        constraints = value["constraints"]
        self.assertIn("撤回或补充只形成新版本", constraints)
        self.assertIn("个人经历在公开说明中必须脱敏", constraints)
        self.assertIn("同一联署不能重复计人数", constraints)
        self.assertIn("跨领域意见允许分别流转", constraints)
        self.assertIn("未定稿条款和内部争议仅向获授权人员开放", constraints)

if __name__ == "__main__":
    unittest.main()
