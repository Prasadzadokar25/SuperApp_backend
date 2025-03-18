
from src.bill_module.parties.model.parties_model import BillbookCustomerInfo
from src.db_config import DbConfig
from flask import jsonify


class PartiesDao:

    def get_parties(self,shop_id):
        
        """
        Fetches all parties (customers) associated with a given shop_id.
        
        Parameters:
        shop_id (int): The ID of the shop whose parties need to be retrieved.
        
        Returns:
        JSON response containing customer data and HTTP status code.
        """

        query='''select * from billbook_customer_info where shop_id=%s'''

        try:
            connection=DbConfig().get_db_connection()
            cursur=connection.cursor()
            cursur.execute(query,(shop_id))
            result=cursur.fetchall()
            # print(result)
            return jsonify({'data':result}),200

        except Exception as e:
             
            return jsonify({f"massage":str(e) }),400
        finally:
            # connection.close()
            cursur.close()



    def create_party(self,customer:BillbookCustomerInfo):
        """
        Inserts a new customer (party) into the database.
        
        Parameters:
        customer (BillbookCustomerInfo): Object containing customer details.
        
        Returns:
        JSON response indicating success or failure.
        """


        query='''insert into billbook_customer_info (customer_name,customer_contact,customer_type,customer_gstin,customer_pan,shop_id) values(%s,%s,%s,%s,%s,%s)'''
        query2='''select * from  billbook_customer_info where customer_contact=%s or customer_name=%s or customer_pan=%s or customer_gstin=%s '''
        try:
            connection=DbConfig().get_db_connection()
            cursur=connection.cursor()
            cursur.execute(query2,(customer.customer_name,customer.customer_contact,customer.customer_pan,customer.customer_gstin))
            result=cursur.fetchall()
            if result:
                return jsonify({"message":"party already exists"}),209
            print(result)
            cursur.execute(query,(customer.customer_name,customer.customer_contact,customer.customer_type.value,customer.customer_gstin,customer.customer_pan,customer.shop_id))
            connection.commit()
            return jsonify({"message":"party added sucessfully!"}),200       
        except Exception as e:
            return jsonify({f"message":str(e)}),400
        finally:
            cursur.close()