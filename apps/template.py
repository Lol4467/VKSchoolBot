# -*- coding: utf-8 -*-
import json

template = { 
    "type": "carousel", 
    "elements": [{ 
            "photo_id": "-109837093_457242811", 
            "action": { 
                "type": "open_photo" 
            }, 
            "buttons": [{ 
                "action": { 
                    "type": "open_link", "link": "https://vk.com", 
                    "label": "Текст кнопки 🌚", 
                    "payload": "{}" 
                } 
            }] 
        }, 
        { 
            "photo_id": "-109837093_457242811", 
            "action": { 
                "type": "open_photo" 
            }, 
            "buttons": [{ 
                "action": { 
                    "type": "text", 
                    "label": "Текст кнопки 2", 
                    "payload": "{}" 
                } 
            }] 
        }, 
        { 
            "photo_id": "-109837093_457242811", 
            "action": { 
                "type": "open_photo" 
            }, 
            "buttons": [{ 
                "action": { 
                    "type": "text", 
                    "label": "Текст кнопки 3", 
                    "payload": "{}" 
                } 
            }] 
        } 
    ] 
}


template = json.dumps(template, ensure_ascii=False).encode('utf-8')
template = str(template.decode('utf-8'))