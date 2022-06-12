class LocatorConverter:
    def __init__(self, attributes):
        """
        attributes : Appium inspector Selected Element의 Copy Attributes to Clipboard '리스트-딕셔너리' 값 찾기
        """
        self.attributes = attributes

    def attribute_find_class(self):
        """
        Attribute 클래스 값 찾기
        """
        try:
            attributes_list = self.attributes
            type_check = isinstance(attributes_list, list)
            # print(type_check)
            result = []
            for data in attributes_list:
                if data['key'].find('class') != -1:
                    result.append(data['value'])
                    string_to_list_result = "".join(result)
                    return string_to_list_result
        except TypeError:
            print("attributes는 List가 Dictionary 형태의 데이터를 가지고 있는 값이어야 합니다.")

    def attribute_find_text_and_resource_id(self):
        """
        Attribute 텍스트 및 리소스 아이디 값 찾기
        """
        try:
            attributes_list = self.attributes
            type_check = isinstance(attributes_list, list)
            # print(type_check)
            result = []
            for data in attributes_list:
                if data['key'].find('text') != -1 and len(data['value']) >= 1:
                    result.append(data['value'])
                    string_to_list_result = "".join(result)
                    attribute_data = f'[@text="{string_to_list_result}"]'
                    return attribute_data
                elif data['key'].find('resource-id') != -1 and len(data['value']) >= 1:
                    result.append(data['value'])
                    string_to_list_result = "".join(result)
                    attribute_data = f'[@resource-id="{string_to_list_result}"]'
                    return attribute_data
        except TypeError:                                                          
            print("attributes는 List가 Dictionary 형태의 데이터를 가지고 있는 값이어야 합니다.")

    def str_locator_create(self):
        """
        str type 로케이터 생성
        """
        create_class = self.attribute_find_class()
        create_attribute = self.attribute_find_text_and_resource_id()
        locator = f'(By.XPATH, \'//{create_class}{create_attribute}\')'
        print(locator)
        return locator

    def tuple_locator_create(self):
        """
        tuple type 로케이터 생성
        """
        create_class = self.attribute_find_class()
        create_attribute = self.attribute_find_text_and_resource_id()
        locator = f'xpath, //{create_class}{create_attribute}'
        convert_string_to_tuple_locator = tuple(map(str, locator.split(', ')))
        print(convert_string_to_tuple_locator)
        return convert_string_to_tuple_locator


if __name__ == '__main__':
    # 테스트
    find_class = LocatorConverter([{"key":"elementId","value":"00000000-0000-000a-ffff-ffff00000061","name":"elementId"},{"key":"index","value":"1","name":"index"},{"key":"package","value":"com.Classting","name":"package"},{"key":"class","value":"android.widget.TextView","name":"class"},{"key":"text","value":"이메일로 로그인","name":"text"},{"key":"checkable","value":"false","name":"checkable"},{"key":"checked","value":"false","name":"checked"},{"key":"clickable","value":"false","name":"clickable"},{"key":"enabled","value":"true","name":"enabled"},{"key":"focusable","value":"false","name":"focusable"},{"key":"focused","value":"false","name":"focused"},{"key":"long-clickable","value":"false","name":"long-clickable"},{"key":"password","value":"false","name":"password"},{"key":"scrollable","value":"false","name":"scrollable"},{"key":"selected","value":"false","name":"selected"},{"key":"bounds","value":"[91,287][989,340]","name":"bounds"},{"key":"displayed","value":"true","name":"displayed"}])
    find_text = LocatorConverter([{"key":"elementId","value":"00000000-0000-000a-ffff-ffff00000061","name":"elementId"},{"key":"index","value":"1","name":"index"},{"key":"package","value":"com.Classting","name":"package"},{"key":"class","value":"android.widget.TextView","name":"class"},{"key":"text","value":"이메일로 로그인","name":"text"},{"key":"checkable","value":"false","name":"checkable"},{"key":"checked","value":"false","name":"checked"},{"key":"clickable","value":"false","name":"clickable"},{"key":"enabled","value":"true","name":"enabled"},{"key":"focusable","value":"false","name":"focusable"},{"key":"focused","value":"false","name":"focused"},{"key":"long-clickable","value":"false","name":"long-clickable"},{"key":"password","value":"false","name":"password"},{"key":"scrollable","value":"false","name":"scrollable"},{"key":"selected","value":"false","name":"selected"},{"key":"bounds","value":"[91,287][989,340]","name":"bounds"},{"key":"displayed","value":"true","name":"displayed"}])
    find_resource_id = LocatorConverter([{"key":"elementId","value":"00000000-0000-000a-0000-01ae000000ac","name":"elementId"},{"key":"index","value":"1","name":"index"},{"key":"package","value":"com.Classting","name":"package"},{"key":"class","value":"android.widget.EditText","name":"class"},{"key":"text","value":"","name":"text"},{"key":"resource-id","value":"mobile-number","name":"resource-id"},{"key":"checkable","value":"false","name":"checkable"},{"key":"checked","value":"false","name":"checked"},{"key":"clickable","value":"true","name":"clickable"},{"key":"enabled","value":"true","name":"enabled"},{"key":"focusable","value":"true","name":"focusable"},{"key":"focused","value":"false","name":"focused"},{"key":"long-clickable","value":"false","name":"long-clickable"},{"key":"password","value":"false","name":"password"},{"key":"scrollable","value":"false","name":"scrollable"},{"key":"selected","value":"false","name":"selected"},{"key":"bounds","value":"[44,264][1036,390]","name":"bounds"},{"key":"displayed","value":"true","name":"displayed"}])

    print(find_class.attribute_find_class())
    print(find_text.attribute_find_text_and_resource_id())
    print(find_resource_id.attribute_find_text_and_resource_id())

    print(find_text.str_locator_create())
    print(type(find_text.str_locator_create()))
    print(find_resource_id.str_locator_create())
    print(type(find_resource_id.str_locator_create()))
    
    print(find_text.tuple_locator_create())
    print(type(find_text.tuple_locator_create()))
    print(find_resource_id.tuple_locator_create())
    print(type(find_resource_id.tuple_locator_create()))

    print(LocatorConverter.__init__.__doc__)
    print(LocatorConverter.attribute_find_class.__doc__)
    print(LocatorConverter.attribute_find_text_and_resource_id.__doc__)
    print(LocatorConverter.str_locator_create.__doc__)
    print(LocatorConverter.tuple_locator_create.__doc__)