

def fullPortScan(self):
    fullTargetInp = self.full_targetinput_1.text()
    subnetMaskLen = self.full_subnetLen.text()
    print(fullTargetInp+subnetMaskLen)
    scanner.scan(hosts=fullTargetInp+subnetMaskLen, arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [{"ip_add":x,"status":scanner[x]['status']['state']} for x in scanner.all_hosts()]
    print(hosts_list)