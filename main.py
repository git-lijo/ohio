from flask import Flask, request
from flask_restful import Resource, Api
from database import create_tables, insert_yearly_values, select_yearly_count_values
from excel_processing import get_yearly_count

app = Flask(__name__)
api = Api(app)

create_tables()


class Demo(Resource):
    def get(self):
        args = dict(request.args)
        well_number = args.get("well", "invalid number")[0]
        if well_number.isdigit():
            well_number = int(well_number)
            yearly_count_data = get_yearly_count(well_number)
            if yearly_count_data:
                county = yearly_count_data["COUNTY"]
                township = yearly_count_data["TOWNSHIP"]
                prod_yr = yearly_count_data["Production Year"]
                wellname = yearly_count_data["WELLNAME"]
                wellno = yearly_count_data["WELLNUMBER"]
                days = yearly_count_data["DAYS"]
                oil_val = yearly_count_data["OIL"]
                gas_val = yearly_count_data["GAS"]
                brine_val = yearly_count_data["BRINE"]
                yr_count_data = select_yearly_count_values(well_number)
                if len(yr_count_data) == 0:
                    insert_yearly_values(well_number, oil_val, gas_val, brine_val, county, township, prod_yr, wellname, wellno, days)
                    return {"oil": oil_val, "gas": gas_val, "brine": brine_val}
                else:
                    for row in yr_count_data:
                        return {"oil": row[1], "gas": row[2], "brine": row[3]}
                    pass
            else:
                return {"message": "Invalid Well Number"}
        else:
            return {"message": "Invalid Well Number"}


api.add_resource(Demo, '/data')

if __name__ == '__main__':
    app.run(debug=True, port=8081)
