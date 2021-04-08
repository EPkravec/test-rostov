class Workload:

    def __init__(self, name, cloud, username, password, ip, aws_access_key_id=None, aws_secret_access_key=None,
                 domen='us-east-1', credentals_box=None):
        self.name = name
        self.cloud = cloud
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.username_aws = username
        self.password_aws = password
        self.domen = domen
        self.ip = ip
        self.credentals_box = credentals_box

    def creat_box(self):
        self.credentals_box = dict.fromkeys(
            [self.cloud], [dict.fromkeys(['aws_access_key_id'], self.aws_access_key_id),
                           dict.fromkeys(['ws_secret_access_key'], self.aws_secret_access_key),
                           dict.fromkeys(['username'], self.username_aws),
                           dict.fromkeys(['password'], self.password_aws),
                           dict.fromkeys(['domen'], self.domen),
                           dict.fromkeys(['ip'], self.ip)]
        )
        return f'{self.credentals_box}'

    def __str__(self):
        return f'Данные по подключению к {self.name}: \n {self.credentals_box}'


class Credentials:

    def __int__(self, workload):
        self.workload = workload().creat_box()

    def balala(self):
        data = self.workload
        for items in data:
            if items == 'aws':
                for values in data['aws']:
                    for key, value in values.items():
                        if key == 'aws_access_key_id':
                            pass
                        elif key == 'aws_secret_access_key':
                            pass
                        elif key == 'ip':
                            self.ip = value
                        elif key == 'username':
                            self.username = value
                        elif key == 'password':
                            self.password = value
                        elif key == 'domen':
                            self.domen = value

    def __str__(self):
        return f'username - {self.username}'


a = Workload(name='awscloud', cloud='aws', username='user1', password='12346576', ip='198.123.24.1')
b = a.creat_box()
# print(a)
print(b)
g = Credentials(workload=a)
print(g)


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
