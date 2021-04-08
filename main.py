class Workload:

    def __init__(self, cloud, username, password, ip, point, size, aws_access_key_id=None, aws_secret_access_key=None,
                 credentals_box=None, domen='us-east-1'):
        self.cloud = cloud
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.username_aws = username
        self.password_aws = password
        self.domen = domen
        self.ip = ip
        self.credentals_box = credentals_box
        self.point = point
        self.size = size

    def creat_box(self):
        if not self.credentals_box:
            self.credentals_box = dict.fromkeys(
                [self.cloud], [dict.fromkeys(['aws_access_key_id'], self.aws_access_key_id),
                               dict.fromkeys(['ws_secret_access_key'], self.aws_secret_access_key),
                               dict.fromkeys(['username'], self.username_aws),
                               dict.fromkeys(['password'], self.password_aws),
                               dict.fromkeys(['domen'], self.domen),
                               dict.fromkeys(['ip'], self.ip),
                               dict.fromkeys(['point'], self.point),
                               dict.fromkeys(['size'], self.size)
                               ]
            )

            data_box = self.credentals_box
            return data_box
        else:
            data_box = self.credentals_box
            return data_box


class Credentials:

    def __init__(self, workload):
        self.workload = workload
        self.username = None
        self.password = None
        self.domen = None
        self.ip = None

    def check_upd(self):
        for items in self.workload:
            if items == 'aws':
                for values in self.workload['aws']:
                    for key, value in values.items():
                        if key == 'username':
                            self.username = value
                        elif key == 'password':
                            self.password = value
                        elif key == 'ip':
                            self.ip = value
                        elif key == 'domen':
                            self.domen = value
        return f'username = {self.username}, password = {self.password}, domen = {self.domen}, ip = {self.ip}'


class MountPoint:

    def __init__(self, workload):
        self.workload = workload
        self.point = None
        self.size = None

    def check_ps(self):
        for items in self.workload:
            if items == 'aws':
                for values in self.workload['aws']:
                    for key, value in values.items():
                        if key == 'point':
                            self.point = value
                        elif key == 'size':
                            self.size = value

        return f'point = {self.point}, size = {self.size}'


a = Workload(cloud='aws', username='user1', password='12346576', ip='198.123.24.1', point='c:\\sd\\sddse',
             size='512').creat_box()
print(a)
b = Credentials(workload=a).check_upd()
print(b)
g = MountPoint(workload=a).check_ps()
print(g)


#
#
# class MigrationTarget:
#
#     def __init__(self):
#         self.type_cloud = ['aws', 'azure', 'vsphere', 'vcloud']
#         # self.credentials =
