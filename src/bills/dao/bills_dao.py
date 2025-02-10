from db_config import get_db_connection
from flask import jsonify

class BillDao:
    
    def get_bill_for_dates(self,shop_id,start_date,end_date):
        
        query = """
                SELECT 
                    bb.bill_id, bb.shop_id, bb.customer_id, bc.customer_name, 
                    bc.customer_contact, bc.customer_type, bc.customer_gstin, 
                    bc.customer_pan, bb.created_date, bb.modified_date, bb.is_paid, bb.status
                FROM billbook_bills AS bb
                INNER JOIN billbook_customer_info AS bc 
                ON bb.customer_id = bc.customer_id
                WHERE DATE(bb.created_date) BETWEEN %s AND %s
                AND bb.shop_id = %s;
            """
        connection = None
        cursor = None    
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute(query, (start_date, end_date, shop_id))  # Pass parameters dynamically
            result = cursor.fetchall()
            if result:
                return result
            return None
        except Exception as e:
            print(e)
            raise Exception(f"(bill_dao):{e}")
        finally:
            connection.close()
            cursor.close()
