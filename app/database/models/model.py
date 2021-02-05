from ... import db

print('init_db')
'''
@现在临时使用
@2021.2.3
'''


class EgsAll(db.Model):
    def __init__(self, sheel_id, time_id, emp):
        self.sheel_id = sheel_id
        self.time_id = time_id

        for i in range(len(emp)):
            # print('_' + str(i+1))
            setattr(self, '_' + str(i+1), emp[i])

    __tablename__ = 'egs_all'
    mysql_row_format = 'DYNAMIC'
    id = db.Column(db.Integer, primary_key=True)
    sheel_id = db.Column(db.Integer, nullable=False, index=True)
    time_id = db.Column(db.Integer, nullable=False, index=True)
    _1 = db.Column('1', db.Text(collation='utf8_general_ci'))
    _2 = db.Column('2', db.Text(collation='utf8_general_ci'))
    _3 = db.Column('3', db.Text(collation='utf8_general_ci'))
    _4 = db.Column('4', db.Text(collation='utf8_general_ci'))
    _5 = db.Column('5', db.Text(collation='utf8_general_ci'))
    _6 = db.Column('6', db.Text(collation='utf8_general_ci'))
    _7 = db.Column('7', db.Text(collation='utf8_general_ci'))
    _8 = db.Column('8', db.Text(collation='utf8_general_ci'))
    _9 = db.Column('9', db.Text(collation='utf8_general_ci'))
    _10 = db.Column('10', db.Text(collation='utf8_general_ci'))
    _11 = db.Column('11', db.Text(collation='utf8_general_ci'))
    _12 = db.Column('12', db.Text(collation='utf8_general_ci'))
    _13 = db.Column('13', db.Text(collation='utf8_general_ci'))
    _14 = db.Column('14', db.Text(collation='utf8_general_ci'))
    _15 = db.Column('15', db.Text(collation='utf8_general_ci'))
    _16 = db.Column('16', db.Text(collation='utf8_general_ci'))
    _17 = db.Column('17', db.Text(collation='utf8_general_ci'))
    _18 = db.Column('18', db.Text(collation='utf8_general_ci'))
    _19 = db.Column('19', db.Text(collation='utf8_general_ci'))
    _20 = db.Column('20', db.Text(collation='utf8_general_ci'))
    _21 = db.Column('21', db.Text(collation='utf8_general_ci'))
    _22 = db.Column('22', db.Text(collation='utf8_general_ci'))
    _23 = db.Column('23', db.Text(collation='utf8_general_ci'))
    _24 = db.Column('24', db.Text(collation='utf8_general_ci'))
    _25 = db.Column('25', db.Text(collation='utf8_general_ci'))
    _26 = db.Column('26', db.Text(collation='utf8_general_ci'))
    _27 = db.Column('27', db.Text(collation='utf8_general_ci'))
    _28 = db.Column('28', db.Text(collation='utf8_general_ci'))
    _29 = db.Column('29', db.Text(collation='utf8_general_ci'))
    _30 = db.Column('30', db.Text(collation='utf8_general_ci'))
    _31 = db.Column('31', db.Text(collation='utf8_general_ci'))
    _32 = db.Column('32', db.Text(collation='utf8_general_ci'))
    _33 = db.Column('33', db.Text(collation='utf8_general_ci'))
    _34 = db.Column('34', db.Text(collation='utf8_general_ci'))
    _35 = db.Column('35', db.Text(collation='utf8_general_ci'))
    _36 = db.Column('36', db.Text(collation='utf8_general_ci'))
    _37 = db.Column('37', db.Text(collation='utf8_general_ci'))
    _38 = db.Column('38', db.Text(collation='utf8_general_ci'))
    _39 = db.Column('39', db.Text(collation='utf8_general_ci'))
    _40 = db.Column('40', db.Text(collation='utf8_general_ci'))
    _41 = db.Column('41', db.Text(collation='utf8_general_ci'))
    _42 = db.Column('42', db.Text(collation='utf8_general_ci'))
    _43 = db.Column('43', db.Text(collation='utf8_general_ci'))
    _44 = db.Column('44', db.Text(collation='utf8_general_ci'))
    _45 = db.Column('45', db.Text(collation='utf8_general_ci'))
    _46 = db.Column('46', db.Text(collation='utf8_general_ci'))
    _47 = db.Column('47', db.Text(collation='utf8_general_ci'))
    _48 = db.Column('48', db.Text(collation='utf8_general_ci'))
    _49 = db.Column('49', db.Text(collation='utf8_general_ci'))
    _50 = db.Column('50', db.Text(collation='utf8_general_ci'))
    _51 = db.Column('51', db.Text(collation='utf8_general_ci'))
    _52 = db.Column('52', db.Text(collation='utf8_general_ci'))
    _53 = db.Column('53', db.Text(collation='utf8_general_ci'))
    _54 = db.Column('54', db.Text(collation='utf8_general_ci'))
    _55 = db.Column('55', db.Text(collation='utf8_general_ci'))
    _56 = db.Column('56', db.Text(collation='utf8_general_ci'))
    _57 = db.Column('57', db.Text(collation='utf8_general_ci'))
    _58 = db.Column('58', db.Text(collation='utf8_general_ci'))
    _59 = db.Column('59', db.Text(collation='utf8_general_ci'))
    _60 = db.Column('60', db.Text(collation='utf8_general_ci'))
    _61 = db.Column('61', db.Text(collation='utf8_general_ci'))
    _62 = db.Column('62', db.Text(collation='utf8_general_ci'))
    _63 = db.Column('63', db.Text(collation='utf8_general_ci'))
    _64 = db.Column('64', db.Text(collation='utf8_general_ci'))
    _65 = db.Column('65', db.Text(collation='utf8_general_ci'))
    _66 = db.Column('66', db.Text(collation='utf8_general_ci'))
    _67 = db.Column('67', db.Text(collation='utf8_general_ci'))
    _68 = db.Column('68', db.Text(collation='utf8_general_ci'))
    _69 = db.Column('69', db.Text(collation='utf8_general_ci'))
    _70 = db.Column('70', db.Text(collation='utf8_general_ci'))
    _71 = db.Column('71', db.Text(collation='utf8_general_ci'))
    _72 = db.Column('72', db.Text(collation='utf8_general_ci'))
    _73 = db.Column('73', db.Text(collation='utf8_general_ci'))
    _74 = db.Column('74', db.Text(collation='utf8_general_ci'))
    _75 = db.Column('75', db.Text(collation='utf8_general_ci'))
    _76 = db.Column('76', db.Text(collation='utf8_general_ci'))
    _77 = db.Column('77', db.Text(collation='utf8_general_ci'))
    _78 = db.Column('78', db.Text(collation='utf8_general_ci'))
    _79 = db.Column('79', db.Text(collation='utf8_general_ci'))
    _80 = db.Column('80', db.Text(collation='utf8_general_ci'))
    _81 = db.Column('81', db.Text(collation='utf8_general_ci'))
    _82 = db.Column('82', db.Text(collation='utf8_general_ci'))
    _83 = db.Column('83', db.Text(collation='utf8_general_ci'))
    _84 = db.Column('84', db.Text(collation='utf8_general_ci'))
    _85 = db.Column('85', db.Text(collation='utf8_general_ci'))
    _86 = db.Column('86', db.Text(collation='utf8_general_ci'))
    _87 = db.Column('87', db.Text(collation='utf8_general_ci'))
    _88 = db.Column('88', db.Text(collation='utf8_general_ci'))
    _89 = db.Column('89', db.Text(collation='utf8_general_ci'))
    _90 = db.Column('90', db.Text(collation='utf8_general_ci'))
    _91 = db.Column('91', db.Text(collation='utf8_general_ci'))
    _92 = db.Column('92', db.Text(collation='utf8_general_ci'))
    _93 = db.Column('93', db.Text(collation='utf8_general_ci'))
    _94 = db.Column('94', db.Text(collation='utf8_general_ci'))
    _95 = db.Column('95', db.Text(collation='utf8_general_ci'))
    _96 = db.Column('96', db.Text(collation='utf8_general_ci'))
    _97 = db.Column('97', db.Text(collation='utf8_general_ci'))
    _98 = db.Column('98', db.Text(collation='utf8_general_ci'))
    _99 = db.Column('99', db.Text(collation='utf8_general_ci'))
    _100 = db.Column('100', db.Text(collation='utf8_general_ci'))
    _101 = db.Column('101', db.Text(collation='utf8_general_ci'))
    _102 = db.Column('102', db.Text(collation='utf8_general_ci'))
    _103 = db.Column('103', db.Text(collation='utf8_general_ci'))
    _104 = db.Column('104', db.Text(collation='utf8_general_ci'))
    _105 = db.Column('105', db.Text(collation='utf8_general_ci'))
    _106 = db.Column('106', db.Text(collation='utf8_general_ci'))
    _107 = db.Column('107', db.Text(collation='utf8_general_ci'))
    _108 = db.Column('108', db.Text(collation='utf8_general_ci'))
    _109 = db.Column('109', db.Text(collation='utf8_general_ci'))
    _110 = db.Column('110', db.Text(collation='utf8_general_ci'))
    _111 = db.Column('111', db.Text(collation='utf8_general_ci'))
    _112 = db.Column('112', db.Text(collation='utf8_general_ci'))
    _113 = db.Column('113', db.Text(collation='utf8_general_ci'))
    _114 = db.Column('114', db.Text(collation='utf8_general_ci'))
    _115 = db.Column('115', db.Text(collation='utf8_general_ci'))
    _116 = db.Column('116', db.Text(collation='utf8_general_ci'))
    _117 = db.Column('117', db.Text(collation='utf8_general_ci'))
    _118 = db.Column('118', db.Text(collation='utf8_general_ci'))
    _119 = db.Column('119', db.Text(collation='utf8_general_ci'))
    _120 = db.Column('120', db.Text(collation='utf8_general_ci'))
    _121 = db.Column('121', db.Text(collation='utf8_general_ci'))
    _122 = db.Column('122', db.Text(collation='utf8_general_ci'))
    _123 = db.Column('123', db.Text(collation='utf8_general_ci'))
    _124 = db.Column('124', db.Text(collation='utf8_general_ci'))
    _125 = db.Column('125', db.Text(collation='utf8_general_ci'))
    _126 = db.Column('126', db.Text(collation='utf8_general_ci'))
    _127 = db.Column('127', db.Text(collation='utf8_general_ci'))
    _128 = db.Column('128', db.Text(collation='utf8_general_ci'))
    _129 = db.Column('129', db.Text(collation='utf8_general_ci'))
    _130 = db.Column('130', db.Text(collation='utf8_general_ci'))
    _131 = db.Column('131', db.Text(collation='utf8_general_ci'))
    _132 = db.Column('132', db.Text(collation='utf8_general_ci'))
    _133 = db.Column('133', db.Text(collation='utf8_general_ci'))
    _134 = db.Column('134', db.Text(collation='utf8_general_ci'))
    _135 = db.Column('135', db.Text(collation='utf8_general_ci'))
    _136 = db.Column('136', db.Text(collation='utf8_general_ci'))
    _137 = db.Column('137', db.Text(collation='utf8_general_ci'))
    _138 = db.Column('138', db.Text(collation='utf8_general_ci'))
    _139 = db.Column('139', db.Text(collation='utf8_general_ci'))
    _140 = db.Column('140', db.Text(collation='utf8_general_ci'))
    _141 = db.Column('141', db.Text(collation='utf8_general_ci'))
    _142 = db.Column('142', db.Text(collation='utf8_general_ci'))
    _143 = db.Column('143', db.Text(collation='utf8_general_ci'))
    _144 = db.Column('144', db.Text(collation='utf8_general_ci'))
    _145 = db.Column('145', db.Text(collation='utf8_general_ci'))
    _146 = db.Column('146', db.Text(collation='utf8_general_ci'))
    _147 = db.Column('147', db.Text(collation='utf8_general_ci'))
    _148 = db.Column('148', db.Text(collation='utf8_general_ci'))
    _149 = db.Column('149', db.Text(collation='utf8_general_ci'))
    _150 = db.Column('150', db.Text(collation='utf8_general_ci'))
    _151 = db.Column('151', db.Text(collation='utf8_general_ci'))
    _152 = db.Column('152', db.Text(collation='utf8_general_ci'))
    _153 = db.Column('153', db.Text(collation='utf8_general_ci'))
    _154 = db.Column('154', db.Text(collation='utf8_general_ci'))
    _155 = db.Column('155', db.Text(collation='utf8_general_ci'))
    _156 = db.Column('156', db.Text(collation='utf8_general_ci'))
    _157 = db.Column('157', db.Text(collation='utf8_general_ci'))
    _158 = db.Column('158', db.Text(collation='utf8_general_ci'))
    _159 = db.Column('159', db.Text(collation='utf8_general_ci'))
    _160 = db.Column('160', db.Text(collation='utf8_general_ci'))
    _161 = db.Column('161', db.Text(collation='utf8_general_ci'))
    _162 = db.Column('162', db.Text(collation='utf8_general_ci'))
    _163 = db.Column('163', db.Text(collation='utf8_general_ci'))
    _164 = db.Column('164', db.Text(collation='utf8_general_ci'))
    _165 = db.Column('165', db.Text(collation='utf8_general_ci'))
    _166 = db.Column('166', db.Text(collation='utf8_general_ci'))
    _167 = db.Column('167', db.Text(collation='utf8_general_ci'))
    _168 = db.Column('168', db.Text(collation='utf8_general_ci'))
    _169 = db.Column('169', db.Text(collation='utf8_general_ci'))
    _170 = db.Column('170', db.Text(collation='utf8_general_ci'))
    _171 = db.Column('171', db.Text(collation='utf8_general_ci'))
    _172 = db.Column('172', db.Text(collation='utf8_general_ci'))
    _173 = db.Column('173', db.Text(collation='utf8_general_ci'))
    _174 = db.Column('174', db.Text(collation='utf8_general_ci'))
    _175 = db.Column('175', db.Text(collation='utf8_general_ci'))
    _176 = db.Column('176', db.Text(collation='utf8_general_ci'))
    _177 = db.Column('177', db.Text(collation='utf8_general_ci'))
    _178 = db.Column('178', db.Text(collation='utf8_general_ci'))
    _179 = db.Column('179', db.Text(collation='utf8_general_ci'))
    _180 = db.Column('180', db.Text(collation='utf8_general_ci'))
    _181 = db.Column('181', db.Text(collation='utf8_general_ci'))
    _182 = db.Column('182', db.Text(collation='utf8_general_ci'))
    _183 = db.Column('183', db.Text(collation='utf8_general_ci'))
    _184 = db.Column('184', db.Text(collation='utf8_general_ci'))
    _185 = db.Column('185', db.Text(collation='utf8_general_ci'))
    _186 = db.Column('186', db.Text(collation='utf8_general_ci'))
    _187 = db.Column('187', db.Text(collation='utf8_general_ci'))
    _188 = db.Column('188', db.Text(collation='utf8_general_ci'))
    _189 = db.Column('189', db.Text(collation='utf8_general_ci'))
    _190 = db.Column('190', db.Text(collation='utf8_general_ci'))
    _191 = db.Column('191', db.Text(collation='utf8_general_ci'))
    _192 = db.Column('192', db.Text(collation='utf8_general_ci'))
    _193 = db.Column('193', db.Text(collation='utf8_general_ci'))
    _194 = db.Column('194', db.Text(collation='utf8_general_ci'))
    _195 = db.Column('195', db.Text(collation='utf8_general_ci'))
    _196 = db.Column('196', db.Text(collation='utf8_general_ci'))
    _197 = db.Column('197', db.Text(collation='utf8_general_ci'))
    _198 = db.Column('198', db.Text(collation='utf8_general_ci'))
    _199 = db.Column('199', db.Text(collation='utf8_general_ci'))
    _200 = db.Column('200', db.Text(collation='utf8_general_ci'))


class FieldName(db.Model):
    __tablename__ = 'field_name'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255, 'utf8_general_ci'), nullable=False)
    field_data_name = db.Column(db.String(255, 'utf8_general_ci'), nullable=False)
    basic_name = db.Column(db.String(255, 'utf8_general_ci'))
    time_id = db.Column(db.ForeignKey('time.id'), nullable=False, index=True)

    time = db.relationship('Time', primaryjoin='FieldName.time_id == Time.id', backref='field_names')


class Sheel(db.Model):
    __tablename__ = 'sheel'

    id = db.Column(db.Integer, primary_key=True)
    sheel_name = db.Column(db.String(255, 'utf8_general_ci'))
    bascil_name = db.Column(db.String(255, 'utf8_general_ci'))
    time_id = db.Column(db.ForeignKey('time.id'), nullable=False, index=True)

    time = db.relationship('Time', primaryjoin='Sheel.time_id == Time.id', backref='sheels')


class Time(db.Model):
    __tablename__ = 'time'

    id = db.Column(db.Integer, primary_key=True)
    creat_time = db.Column(db.DateTime, nullable=False)
    _as = db.Column('as', db.String(255, 'utf8_general_ci'))
