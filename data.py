class OrdersUrl:
    main_url = 'https://qa-scooter.praktikum-services.ru'
    main_orders_url = '/api/v1/orders'

class CourierUrl:
    main_url = 'https://qa-scooter.praktikum-services.ru'
    login_url = '/api/v1/courier/login'
    courier_url = '/api/v1/courier/'

class CourierErrors:
    error_count_orders_no_data = "Недостаточно данных для поиска"
    error_count_orders_no_such_user = "Курьер не найден"
    error_login_no_data = "Недостаточно данных для входа"
    error_create_no_data = "Недостаточно данных для создания учетной записи"
    error_create_already_exist = "Этот логин уже используется. Попробуйте другой."

class DataOrdered:
    order_color_black = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-02-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }

    order_color_grey = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-02-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "GREY"
        ]
    }

    order_color_black_and_grey = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-02-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK",
            "GREY"
        ]
    }

    order_no_color = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-02-06",
        "comment": "Saske, come back to Konoha",
        "color": [
        ]
    }
