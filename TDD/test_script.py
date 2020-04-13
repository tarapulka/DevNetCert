### To run the test use:
###   python3 -m unittest test_script.py
import  unittest
import re


class TestCustomerDetails(unittest.TestCase):
    def test_cu_name(self):
        ### Our script has a class ConfigurationParser, which will have method ParseCuNames
        cp = ConfigurationParser()
        ### expected names which is present on config.txt
        exp_names= ['CUSTOMER_A','CUSTOMER_B']
        ### names return by our code
        parsed_names = cp.ParseCuNames()
        ### Names returned by our code should be in list
        self.assertEqual(list,type(parsed_names))
        ### Names returned by our code should be the same as expected names (exp_names)
        self.assertEqual(exp_names,parsed_names)

    def test_cust_vlan(self):
        ### Our script has a class ConfigurationParser, which will have method ParseCuNames
        cp = ConfigurationParser()
        ### Example of the customer name from config.txt
        cu_name = "CUSTOMER_A"
        ### Example of the vlan for CUSTOMER_A from config.txt
        exp_vlan = ['100']
        ### ParseVlan will return a vlan number based on the give customer name
        parsed_vlan = cp.ParseVlan(cu_name)
        ### Compare manually checked VLAN (exp_vlan) with the one calculated by the script (parsed_vlan)
        self.assertEqual(exp_vlan,parsed_vlan)




class ConfigurationParser:
    ### my class which will implement the desired functionality
    deviceConfig = open("config.txt","r").read()

    def ParseCuNames(self):
        ### Regular expression to find the Customer name from 'ip vrf <Customer Name>' output
        cuNamePattern = r"ip vrf ([a-zA-Z_]+)\n"
        ### findall with groups returns only matched group value.
        cuNames = re.findall(cuNamePattern,deviceConfig)
        return cuNames

    def ParseVlan(self, cuName):
        ### Regex to find vlan number which is the same as sub interface number
        intPattern=r"interface GigabitEthernet0\/0.([0-9]+)\n\s+encapsulation\s+dot1Q [0-9]+\n\s+ip vrf forwarding %s" % (cuName)
        ### Apply regex to the file to get vlan numbers
        allCuSubInterfaces = re.findall(intPattern,deviceConfig)
        return allCuSubInterfaces
