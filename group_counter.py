from collections import defaultdict


data = defaultdict(list,
            {'MAST30034': [['rsanchezjime@student.unimelb.edu.au ',
               'godbole@student.unimelb.edu.au',
               'kevin.tang1@student.unimelb.edu.au'],
              ['vanessagraci@student.unimelb.edu.au',
               'marcou@student.unimelb.edu.au',
               'wenhany@student.unimelb.edu.au']],
             'MAST30027': [['rsanchezjime@student.unimelb.edu.au ',
               'godbole@student.unimelb.edu.au',
               'vanessagraci@student.unimelb.edu.au',
               'marcou@student.unimelb.edu.au',
               'wenhany@student.unimelb.edu.au']],
             'MAST20005': [['Hanshit@student.unimelb.edu.au',
               'ryanwonhail@student.unimelb.edu.au',
               'thihongminhd@student.unimelb.edu.au'],
              ['Ppulipaka@student.unimelb.edu.au ',
               'dponder@student.unimelb.edu.au',
               'appatha@student.Unimelb.edu.au '],
              'N/A'],
             'INFO30006': ['N/A'],
             'SCIE20001': [['ryanwonhail@student.unimelb.edu.au',
               'jeanmaylynnk@student.unimelb.edu.au',
               'Ppulipaka@student.unimelb.edu.au ',
               'appatha@student.Unimelb.edu.au ']],
             'MAST10006': [['sanjayr@student.unimelb.edu.au',
               'fujimotok@student.unimelb.edu.au',
               'ngocthaonhin@student.unimelb.edu.au'],
              ['loucelp@student.unimelb.edu.au',
               'mpeeterswill@student.unimelb.edu.au',
               'dpalexander@student.unimelb.edu.au'],
              ['hweerawardan@student.unimelb.edu.au',
               'rcchao@student.unimelb.edu.au',
               'phanminhquan@student.unimelb.edu.au']],
             'MAST10010': [['sanjayr@student.unimelb.edu.au',
               'fujimotok@student.unimelb.edu.au',
               'chinghongc@student.unimelb.edu.au'],
              ['ayuxin@student.unimelb.edu.au',
               'ankhangl@student.unimelb.edu.au',
               'yasina@student.unimelb.edu.au'],
              'N/A'],
             'COMP10002': [['sanjayr@student.unimelb.edu.au',
               'hanluo3@student.unimelb.edu.au',
               'chinghongc@student.unimelb.edu.au',
               'panankatham@student.unimelb.edu.au'],
              ['ngocthaonhin@student.unimelb.edu.au',
               'loucelp@student.unimelb.edu.au',
               'ehhow@student.unimelb.edu.au'],
              ['ayuxin@student.unimelb.edu.au',
               'Amoncherry@student.unimelb.edu.au',
               'ankhangl@student.unimelb.edu.au'],
              ['mpeeterswill@student.unimelb.edu.au',
               'yasina@student.unimelb.edu.au',
               'luyeeb@student.unimelb.edu.au'],
              ['hexue@student.unimelb.edu.au',
               'zhangrl@student.unimelb.edu.au',
               'dpalexander@student.unimelb.edu.au'],
              ['ahareesbashe@student.unimelb.edu.au',
               'rcchao@student.unimelb.edu.au',
               'seanzhongmin@student.unimelb.edu.au'],
              'N/A'],
             'ECON10003': ['N/A'],
             'MAST90104': [['chyu3@student.unimelb.edu.au',
               'sbarahate@student.unimelb.edu.au',
               'dponder@student.unimelb.edu.au']],
             'MAST90138': [['chyu3@student.unimelb.edu.au',
               'sbarahate@student.unimelb.edu.au',
               'qingyuan3@student.unimelb.edu.au ',
               'huixchen@student.unimelb.edu.au',
               'hsu.p@student.unimelb.edu.au']],
             'COMP90051': [['chyu3@student.unimelb.edu.au',
               'thanhnguyenp@student.unimelb.edu.au',
               'xuxue@student.unimelb.edu.au',
               'shengyangs@student.unimelb.edu.au']],
             'SCIE30002': ['N/A'],
             'FNCE30010': ['N/A'],
             'MAST10001': ['N/A'],
             'SCIE10005': ['N/A'],
             'MAST10005': ['N/A'],
             'COMP10001': ['N/A'],
             'BLAW10001': [['jeanmaylynnk@student.unimelb.edu.au',
               'thihongminhd@student.unimelb.edu.au',
               'Ppulipaka@student.unimelb.edu.au ']],
             'COMP90089': ['N/A'],
             'MAST10021': [['hanluo3@student.unimelb.edu.au',
               'ankhangl@student.unimelb.edu.au',
               'zhangrl@student.unimelb.edu.au']],
             'COMP20008': [['hanluo3@student.unimelb.edu.au',
               'mpawlus@student.unimelb.edu.au',
               'loucelp@student.unimelb.edu.au'],
              ['ehhow@student.unimelb.edu.au',
               'pchoudhury@student.unimelb.edu.au',
               'Amoncherry@student.unimelb.edu.au'],
              ['qingyuan3@student.unimelb.edu.au ',
               'Ppulipaka@student.unimelb.edu.au ',
               'appatha@student.Unimelb.edu.au ']],
             'MUSI10221': ['N/A'],
             'MAST10007': [['chinghongc@student.unimelb.edu.au',
               'ehhow@student.unimelb.edu.au',
               'ayuxin@student.unimelb.edu.au'],
              ['Amoncherry@student.unimelb.edu.au',
               'yasina@student.unimelb.edu.au',
               'dpalexander@student.unimelb.edu.au'],
              ['ahareesbashe@student.unimelb.edu.au',
               'seanzhongmin@student.unimelb.edu.au',
               'phanminhquan@student.unimelb.edu.au']],
             'LAWS10009': ['N/A'],
             'MUSI20206': ['N/A'],
             'COMP20003': [['thihongminhd@student.unimelb.edu.au',
               'mpawlus@student.unimelb.edu.au',
               'hoangthanhla@student.unimelb.edu.au',
               'baquyenc@student.unimelb.edu.au']],
             'SWEN20003': [['thihongminhd@student.unimelb.edu.au',
               'hoangthanhla@student.unimelb.edu.au',
               'baquyenc@student.unimelb.edu.au']],
             'BIOL10011': ['N/A'],
             'ECON20005': ['N/A'],
             'COMP90014': ['N/A'],
             'COMP90086': ['N/A'],
             'MAST90083': [['xuxue@student.unimelb.edu.au',
               'qingyuan3@student.unimelb.edu.au ',
               'huixchen@student.unimelb.edu.au',
               'shengyangs@student.unimelb.edu.au',
               'hsu.p@student.unimelb.edu.au']],
             'COMP90054': [['xuxue@student.unimelb.edu.au',
               'shengyangs@student.unimelb.edu.au',
               'hsiehw@student.unimelb.edu.au']],
             'COMP90007': ['N/A'],
             'ARCH10001': ['N/A'],
             'MAST20026': [['mpawlus@student.unimelb.edu.au',
               'wongsok@student.unimelb.edu.au',
               'baquyenc@student.unimelb.edu.au',
               'rarain@student.unimelb.edu.au']],
             'HPSC10001': ['N/A'],
             'INFO20003': [['ehhow@student.unimelb.edu.au',
               'Liuly@student.unimelb.edu.au',
               'wongsok@student.unimelb.edu.au',
               'hoangthanhla@student.unimelb.edu.au']],
             'PHYC10008': ['N/A'],
             'SCIE10004': [['pchoudhury@student.unimelb.edu.au',
               'ahareesbashe@student.unimelb.edu.au',
               'seanzhongmin@student.unimelb.edu.au']],
             'MUSI20225': ['N/A'],
             'ACCT10002': ['N/A'],
             'ISYS10001': ['N/A'],
             'FNCE20003': ['N/A'],
             'ERTH10002': ['N/A'],
             'ENGL10001': ['N/A'],
             'MAST90125': ['N/A'],
             'FNCE20005': ['N/A'],
             'MAST30021': ['N/A'],
             'MAST20022': ['N/A'],
             'PHIL30043': ['N/A'],
             'MAST10009': ['N/A'],
             'ENGR10006': ['N/A'],
             'PSYC20009': ['N/A'],
             'COMP90038': ['N/A'],
             'INFO90002': ['N/A'],
             'JAPN10002': ['N/A'],
             'ECON90033': ['N/A'],
             'ECON90034': ['N/A'],
             'ECOM90025': ['N/A'],
             'ECOM90004': ['N/A'],
             'CCDP10003': ['N/A'],
             'GEOM90007': ['N/A'],
             'COMP90043': ['N/A'],
             'ACCT10001': ['N/A'],
             'MULT20015': ['N/A'],
             'COMP90072': ['N/A'],
             'PHYC90006': ['N/A'],
             'PHYC90013': ['N/A'],
             'PHYC90029': ['N/A'],
             'MAST20004': ['N/A'],
             'MAST20018': ['N/A'],
             'ECON10004': ['N/A'],
             'MAST30022': ['N/A']})

# Count the number of groups in each subject (excluding 'N/A' groups)
num_groups_per_subject = {key: len(value) for key, value in data.items() if value[0] != 'N/A'}

# Count the total number of groups across all subjects (excluding 'N/A' groups)
total_groups = sum(num_groups_per_subject.values())

# Print the result
print(num_groups_per_subject)
print("Total number of groups:", total_groups)
