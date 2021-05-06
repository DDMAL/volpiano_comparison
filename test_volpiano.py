import unittest
import volpiano

obtainGT = [
    "1---h--h--h---3",
    "1---h--h--h77---3",
    "1---h---gh--h--h---3",
    "1---g--g--g7---3",
    "1---g--g--g---3",
    "1---g--g--g7---3",
    "1---lmnml7---3",
    "1---d---e--f---3",
    "1---g---hij--hgf---3",
    "1---f--f--e---3",
    "1---e7---g--h7---3",
    "1---f--fe---g7---3",
    "1---e---g--h7---3",
    "1---h--h--h7---3",
    "1---ghg-gf---fg7---3",
    "1---e---g--h7---3",
    "1---j---l--m7---3",
    "1---e---g--h---3",
    "1---j---l--m7---3",
    "1---e---g--h777---3",
    "1---ffe---d--c---3",
    "1---f--g--gh--gf---3",
    "1---e---g--h7---3",
    "1---f--f--e---g7---3",
    "1---f--f--e7---3",
    "1---j--l--m7---3",
    "1---j---l--m7---3",
    "1---e---g--h7---3",
    "1---f--f--e7---3",
    "1---fgf---e--g7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---h---g--h7---3",
    "1---j---l--m7---3",
    "1---h---g--h---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h---3",
    "1---h--h--hghgf7---3",
    "1---g---h7---3",
    "1---h--h--h7---3",
]

validateFakeGT = [
    "---w-OB--4K--KB-kW-v",
    "-H--w---o-a-D-HFR-9-",
    "--4-E--Su-zc5--X-G-1",
    "-[uC-----D--kO-5----",
    "--e-pf]a----5E-5-6w-",
    "---Y--)--5v-(-W--Z-y",
    "1----au--2-----z,---",
    "-1---[------.----X--",
    "-U--0]O-qT--A-QVV--u",
    "WC-f-6---xO4-p,-----",
]

compareGT = [
    0.9375,
    0.8571428571428571,
    0.7741935483870968,
    0.8,
    0.7741935483870968,
    0.5517241379310345,
    0.7741935483870968,
    0.8,
    0.8,
    0.6666666666666666,
    0.7272727272727273,
    0.6875,
    0.967741935483871,
    0.6857142857142857,
    0.6875,
    0.75,
    0.8387096774193549,
    0.75,
    0.6470588235294118,
    0.7272727272727273,
    0.6285714285714286,
    0.6875,
    0.6857142857142857,
    0.7741935483870968,
    0.7741935483870968,
    0.75,
    0.6875,
    0.7741935483870968,
    0.7058823529411765,
    0.6875,
    0.6875,
    0.6875,
    0.6875,
    0.6875,
    0.6875,
    0.6875,
    0.875,
    0.75,
    0.9032258064516129,
    0.6875,
    0.6875,
    0.6875,
    0.6875,
    0.6875,
    0.8387096774193549,
    0.8571428571428571,
    0.7586206896551724,
    0.967741935483871,
]


class TestVolpiano(unittest.TestCase):
    def test_volpiano_obtain(self):
        volpianos = volpiano.obtain(maxLength=20)
        self.assertEqual(set(volpianos), set(obtainGT))

    def test_volpiano_validate(self):
        for idx, v in enumerate(obtainGT):
            with self.subTest(true_volpiano_idx=idx):
                self.assertTrue(volpiano.validate(v))
        for idx, v in enumerate(validateFakeGT):
            with self.subTest(fake_volpiano_idx=idx):
                self.assertFalse(volpiano.validate(v))

    def test_volpiano_compare(self):
        gt = obtainGT
        scores = [volpiano.compare(gt[0], vi) for vi in gt[1:]]
        self.assertAlmostEqual(scores, compareGT)
