class Workload:

    def __init__(self, cloud, username, password, ip, aws_access_key_id=None, aws_secret_access_key=None,
                 credentals_box=None, domen='us-east-1'):
        self.cloud = cloud
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.username_aws = username
        self.password_aws = password
        self.domen = domen
        self.ip = ip
        self.credentals_box = credentals_box

    def creat_box(self):
        if not self.credentals_box:
            self.credentals_box = dict.fromkeys(
                [self.cloud], [dict.fromkeys(['aws_access_key_id'], self.aws_access_key_id),
                               dict.fromkeys(['ws_secret_access_key'], self.aws_secret_access_key),
                               dict.fromkeys(['username'], self.username_aws),
                               dict.fromkeys(['password'], self.password_aws),
                               dict.fromkeys(['domen'], self.domen),
                               dict.fromkeys(['ip'], self.ip)]
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

    def check_upd(self):
        for items in self.workload:
            if items == 'aws':
                for values in self.workload['aws']:
                    for key, value in values.items():
                        if key == 'username':
                            self.username = value
                        elif key == 'password':
                            self.password = value
                        elif key == 'domen':
                            self.domen = value
        return f'username = {self.username}, password = {self.password}, domen = {self.domen}'


a = Workload(cloud='aws', username='user1', password='12346576', ip='198.123.24.1').creat_box()
g = Workload(cloud='aws', username='user1', password='12346576', ip='198.123.24.1')
g = g.creat_box()
print(g)
b = Credentials(workload=a).check_upd()
print(b)


# class MountPoint:
#
#     def __int__(self):
#         self.name_point_mount = 'c:\ '
#         self.total_size_volume = int()
#
#
# class Source:
#
#     def __init__(self):
#         self.credentials = None
#         self.workload = None
#
#     def cheсk(self):
#         if self.workload.ip is None or self.credentials.username is None or self.credentials.password is None:
#             print('отсутсвуют необходимые данные')
#
#
# class MigrationTarget:
#
#     def __init__(self):
#         self.type_cloud = ['aws', 'azure', 'vsphere', 'vcloud']
#         # self.credentials =
