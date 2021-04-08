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


class Credentials:

    def __init__(self, workload):
        self.workload = workload
        self.username = None
        self.password = None
        self.domen = None
        self.ip = None

    def check_upd(self):
        list_upid = []
        for items in self.workload:
            if items == 'aws':
                for values in self.workload['aws']:
                    for key, value in values.items():
                        if key == 'username':
                            self.username = value
                            list_upid.append(self.username)
                        elif key == 'password':
                            self.password = value
                            list_upid.append(self.password)
                        elif key == 'domen':
                            self.domen = value
                        elif key == 'ip':
                            self.ip = value
                            list_upid.append(self.ip)

        return list_upid


class MountPoint:

    def __init__(self, workload):
        self.workload = workload
        self.cloud = None
        self.point = None
        self.size = None

    def check_ps(self):
        list_i = []
        list_p = []
        for items in self.workload:
            if items == 'aws':
                self.cloud = items
                list_i.append(self.cloud)
                for values in self.workload['aws']:
                    for key, value in values.items():
                        if key == 'point':
                            self.point = value
                            list_p.append(self.point)
                        elif key == 'size':
                            self.size = value

        return list_i, list_p


class Source:

    def __init__(self, credentials):
        self.check = credentials

    def check_upi(self):
        for i in self.check:
            if i != None:
                return True
            else:
                print('Error: absent username/password/ip')


class MigratoinTarget:

    def __init__(self, mountPoint):
        self.cloud = mountPoint

    def check_i(self):
        if self.cloud != ['aws'] and self.cloud != ['azure'] and self.cloud != ['vsphere'] and self.cloud != ['vcloud']:
            print('Error: connecting to the wrong cloud')
        else:
            return True


# class Migration:


a = Workload(cloud='aws', username='user1', password='12346576', ip='198.123.24.1', point='c:\\sd\\sddse',
             size='512').creat_box()

b = Credentials(workload=a).check_upd()

g_1 = MountPoint(workload=a).check_ps()[0]

h = Source(credentials=b).check_upi()

e = MigratoinTarget(mountPoint=g_1).check_i()