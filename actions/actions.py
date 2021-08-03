import json
import requests
import pprint
from time import sleep
from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


global global_dic
global ent_list


global_dic={}
ent_list=[]


class ActionFindHotel(Action):

   
    def name(self) -> Text:
        return "action_find_hotels"

    
    currency = "USD"
    headers = {
            'x-rapidapi-key': "cf03cdb80emshcfe16b58ab7e55ap17a505jsn17df98d33df1",
            'x-rapidapi-host': "booking-com.p.rapidapi.com"
    }
    pp = pprint.PrettyPrinter()
    prototype_mode = 0

    destinations_selection_dict = {}
    
    # In[5]:


    def destination_selection(self,destination):
        currency = "USD"
        headers = {
                'x-rapidapi-key': "cf03cdb80emshcfe16b58ab7e55ap17a505jsn17df98d33df1",
                'x-rapidapi-host': "booking-com.p.rapidapi.com"
        }
      
        url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"

        querystring = {"locale":"en-us","name": destination}

        response = requests.request("GET", url, headers=headers, params=querystring)

        json = response.json()

        destinations_selection_dict = {}
        for i in json:
            destinations_selection_dict[i["dest_id"]] = [i["label"], i["dest_type"]]
        try:
            if prototype_mode == 1:
                print(destinations_selection_dict)
        except:
            pass
        return destinations_selection_dict


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        _intent=tracker.latest_message['intent'].get('name')
        print("Intent of user message predicted by Rasa ",_intent)

        print(tracker.latest_message['text']) # to get user typed message
        intent_found = json.dumps(tracker.latest_message['response_selector'][_intent]['ranking'][0]['intent_response_key'], indent=4)
        print("retrieval we found (i.e intent response key ) ",intent_found)

        # intent_found = f'utter_{eval(intent_found)}'
        dispatcher.utter_message(text="We are making a list of places for you...")

        ent = tracker.latest_message['entities']
        print ("entity value found", ent)

        
        for e in ent:
            print(e['value'])
            
            if (e['entity']=='check_in_date'  and ('check_in_date' in ent_list ) ):
                # print ("check-in full")
                global_dic['check_out_date']=e['value']
                ent_list.append('check_out_date')

            else :
                global_dic[e['entity']]=e['value']
                ent_list.append(e['entity'])
        print(global_dic)
        print (ent_list)
        
        

        slots= tracker.slots
        # print(slots)

        for i in ent_list:          
            if tracker.slots[i] == None:
                tracker.slots[i]= global_dic[i]


        
        
        

        


        SlotSet(key = "intent_button", value= None )

        if (tracker.slots['destination']== None):
                print(tracker.slots['destination'])
                dispatcher.utter_message(text="Please provide your..")
                dispatcher.utter_message(text="Destination (hotel city)")
                sleep(3)
                print(tracker.slots['destination'])
                print(tracker.slots['check_in_date'])
                print(tracker.slots['check_out_date'])


        elif (tracker.slots['check_in_date']== None):
                print(tracker.slots['destination'])
                dispatcher.utter_message(text="Please provide your..")
                dispatcher.utter_message(text="Check-in date(yyyy-mm-dd)")
                sleep(3)
                print(tracker.slots['destination'])
                print(tracker.slots['check_in_date'])
                print(tracker.slots['check_out_date'])

        elif (tracker.slots['check_out_date']== None):
                print(tracker.slots['destination'])
                dispatcher.utter_message(text="Please provide your..")
                dispatcher.utter_message(text="Check-out date(yyyy-mm-dd)")
                sleep(3)
                # print("check-out date: "+ (tracker.latest_message['text']))
                print(tracker.slots['destination'])
                print(tracker.slots['check_in_date'])
                print(tracker.slots['check_out_date'])



        else :
            print(tracker.slots)
            dest= self.destination_selection(tracker.slots['destination'])            
            dest_id= list(dest)
            dest_values= list(dest.values())
            
            
            
            # print(dest_values)

            if (len(dest )>=3):
                buttons = [
                {"payload":"/ok{\"intent_button\": \"" +  str(dest_id[0])+"."+str(dest_values[0][1]) + "\"}","title":str(dest_values[0][0])},
                {"payload":"/ok{\"intent_button\": \"" +  str(dest_id[1]) +"."+str(dest_values[1][1]) + "\"}","title":str(dest_values[1][0])},
                {"payload":"/ok{\"intent_button\": \"" +  str(dest_id[2]) +"."+str(dest_values[2][1]) + "\"}","title":str(dest_values[2][0])}
                
                ]
                dispatcher.utter_message(text="List of destinations",buttons=buttons)

            elif (len(dest)==2):
                buttons = [
                {"payload":"/ok{\"intent_button\": \"" +  str(dest_id[0]) + "."+str(dest_values[0][1]) +"\"}","title":str(dest_values[0][0])},
                {"payload":"/ok{\"intent_button\": \"" +  str(dest_id[1]) +"."+str(dest_values[1][1]) + "\"}","title":str(dest_values[1][0])}
                
                
                ]
                dispatcher.utter_message(text="List of destinations",buttons=buttons)
                
            elif(len(dest )==1):
                buttons = [
                {"payload":"/ok{\"intent_button\": \"" +  str(dest_id[0]) +"."+str(dest_values[0][1]) + "\"}","title":str(dest_values[0][0])}]

                dispatcher.utter_message(text="List of destinations",buttons=buttons)

            

            # print(tracker.slots['intent_button'])



        
        return []



class hotelsAction(Action):
        
        def name(self) -> Text:
            return "action_hotel"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            print(tracker.slots)
            dispatcher.utter_message(text="Perfect!!")
            dispatcher.utter_message(text="Preparing list of hotels...")
            dispatcher.utter_message(text="Please provide Number of rooms required!!")
            
            

            
            
            return []

class hotels_API_Action(Action):
    def name(self) -> Text:
        return "action_list_hotels"


    currency = "USD"
    headers = {
            'x-rapidapi-key': "cf03cdb80emshcfe16b58ab7e55ap17a505jsn17df98d33df1",
            'x-rapidapi-host': "booking-com.p.rapidapi.com"
    }
    pp = pprint.PrettyPrinter()
    prototype_mode = 0

    
    
    # In[5]:

    def hotel_selection(self,check_in, check_out, dest_id,dest_type,number_of_people,number_of_rooms, order_by = "price"):
        
        # dest_type = dest2[dest_id][1]
        
        currency = "USD"
        headers = {
                'x-rapidapi-key': "cf03cdb80emshcfe16b58ab7e55ap17a505jsn17df98d33df1",
                'x-rapidapi-host': "booking-com.p.rapidapi.com"
        }
        pp = pprint.PrettyPrinter()
        prototype_mode = 0

        url = "https://booking-com.p.rapidapi.com/v1/hotels/search"

        querystring = {"units":"metric",
                    "checkin_date":check_in,
                    "checkout_date":check_out,
                    "filter_by_currency": currency,
                    "adults_number":number_of_people,
                    "room_number":number_of_rooms,
                    "dest_id":dest_id,
                    "locale":"en-us",
                    "dest_type":dest_type,
                    "order_by":order_by
                    }

        response = requests.request("GET", url, headers=headers, params=querystring)

        json = response.json()

        hotels_selection_dict = {}
        for i in range(0, 5):
            hotels_selection_dict[json["result"][i]["hotel_id"]] =  [json["result"][i]["hotel_name"],
                                        str(round(json["result"][i]["min_total_price"], 2)) + " " + json["result"][i]["price_breakdown"]["currency"],
                                        json["result"][i]["url"], json["result"][i]["main_photo_url"]]
        try:
            if prototype_mode == 1:
                print(hotels_selection_dict)
        except:
            pass
        return hotels_selection_dict




    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print(tracker.slots)
        _intent=tracker.latest_message['intent'].get('name')
        print("Intent of user message predicted by Rasa ",_intent)

        print(tracker.latest_message['text']) # to get user typed message
        intent_found = json.dumps(tracker.latest_message['response_selector'][_intent]['ranking'][0]['intent_response_key'], indent=4)
        print("retrieval we found (i.e intent response key ) ",intent_found)

        # intent_found = f'utter_{eval(intent_found)}'
        dispatcher.utter_message(text="We are making a list of places for you...")

        ent = tracker.latest_message['entities']
        print ("entity value found", ent)

        for e in ent:
            print(e['value'])
        
            
            if (e['entity']=='rooms'  and ('rooms' in ent_list ) ) :
                global_dic['people']=e['value']
                ent_list.append('people')

            elif (e['entity']=='people' and ('rooms'in ent_list)):
                global_dic['people']=e['value']
                ent_list.append('people')

            elif(e['entity']=='people' and ('people'in ent_list)):
                global_dic['rooms']=e['value']
                ent_list.append('rooms')
            
            elif(e['entity']=='people'):
                global_dic['rooms']=e['value']
                ent_list.append('rooms')

            else :
                global_dic[e['entity']]=e['value']
                ent_list.append(e['entity'])

        print(global_dic)
        print (ent_list)

        # for e in ent:
        #     print(e['value'])
            
        #     if (e['entity']=='rooms'):
        #         if('people' in ent_list  == False):
        #         # print ("check-in full")
        #             global_dic['people']=e['value']
        #             ent_list.append('check_out_date')

        #     else :
        #         global_dic[e['entity']]=e['value']
        #         ent_list.append(e['entity'])
        # print(global_dic)
        # print (ent_list)


        slots= tracker.slots
        print(slots)
        # print(" i am in last functiom")
        print (ent_list)
        

        for i in ent_list:
            print(i)

        
        # print(slots)
        for i in ent_list:          
            if tracker.slots[i] == None:
                tracker.slots[i]= global_dic[i]

        print(slots)


        if (tracker.slots['rooms']== None):
            print(tracker.slots['rooms'])
            dispatcher.utter_message(text="Please provide..")
            dispatcher.utter_message(text="Number of rooms required!")
            sleep(3)
            print(slots)
                


        elif (tracker.slots['people']== None):
            print(tracker.slots['people'])
            dispatcher.utter_message(text="Please provide your..")
            dispatcher.utter_message(text="Number of people!")
            sleep(3)
            print(slots)

        
        # print(dest)
        else:
            print(tracker.slots['intent_button'])
            print(tracker.slots)
            destselected= tracker.slots['intent_button'][0].split(".")[0]
            desttype= tracker.slots['intent_button'][0].split(".")[1]

            print(destselected,desttype)

            hotels= self.hotel_selection(tracker.slots['check_in_date'],tracker.slots['check_out_date'],destselected,desttype,tracker.slots['people'],tracker.slots['rooms'])
            
            hotel_id= list(hotels)
            hotel_values= list(hotels.values())
        
            # dest_id= list(dest)
            # print (dest_id)
            # dest_values= list(dest.values())
            
            for x in range(0, len(hotel_id)):
                dispatcher.utter_message(text=""+str(hotel_values[x][0])+"\n\t \n Price:"+ str(hotel_values[x][1])+" \n\t \n Booking Link: [Click here]("+ str(hotel_values[x][2])+")"+"\n\t \n ", image=""+str(hotel_values[x][3]))
            dispatcher.utter_message(text="Hope so, this was helpful, for more detailed infromation check out the website!! Bye...")

            # buttons = [
            # {"payload":"/confirm{\"hotel_id\": \"" +  str(hotel_id[0]) + "\"}","title":str(hotel_values[0][0])+" \n "+ str(hotel_values[0][1])+" \n "+"Booking Link: [Click here]("+ str(hotel_values[0][2])+")"+" \n "+"![]("+str(hotel_values[0][3])+")"},
            # {"payload":"/confirm{\"hotel_id\": \"" +  str(hotel_id[1])  + "\"}","title":str(hotel_values[1][0])},
            # {"payload":"/confirm{\"hotel_id\": \"" +  str(hotel_id[2])  + "\"}","title":str(hotel_values[2][0])}
            
            # ]
            # dispatcher.utter_message(text="List of destinations",buttons=buttons)
                

        return []

       


