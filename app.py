from flask import (
    Flask, 
    jsonify, 
    render_template, 
    request, 
    redirect)
import pandas as pd

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
from flask_sqlalchemy import SQLAlchemy
# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/belly_button_biodiversity.sqlite"

db = SQLAlchemy(app)

class Otu(db.Model):
    __tablename__ = 'taxonomic_units'

    otu_id = db.Column(db.Integer, primary_key=True)
    lowest_taxonomic_unit_found = db.Column(db.String)
    
    def __repr__(self):
        return f"ID: {self.otu_id}, NAME: {self.lowest_taxonomic_unit_found}"

class Metadata(db.Model):
    __tablename__ = 'metadata'

    sampleid = db.Column(db.String, primary_key=True)
    ethnicity = db.Column(db.String)
    gender = db.Column(db.String)
    age = db.Column(db.Float)
    wfreq = db.Column(db.Float)
    bbtype = db.Column(db.String)
    location = db.Column(db.String)
    
    def __repr__(self):
        return f"ID: {self.SAMPLEID}, {self.ETHNICITY} {self.GENDER}, (self.AGE), {self.LOCATION} type: {self.BBTYPE}, wfreq: {self.WFREQ}"

class Sample(db.Model):
    __tablename__ = 'samples'

    otu_id = db.Column(db.Integer, primary_key=True)
    BB_940 = db.Column(db.Integer)
    BB_941 = db.Column(db.Integer)
    BB_943 = db.Column(db.Integer)
    BB_944 = db.Column(db.Integer)
    BB_945 = db.Column(db.Integer)
    BB_946 = db.Column(db.Integer)
    BB_947 = db.Column(db.Integer)
    BB_948 = db.Column(db.Integer)
    BB_949 = db.Column(db.Integer)
    BB_950 = db.Column(db.Integer)
    BB_952 = db.Column(db.Integer)
    BB_953 = db.Column(db.Integer)
    BB_954 = db.Column(db.Integer)
    BB_955 = db.Column(db.Integer)
    BB_956 = db.Column(db.Integer)
    BB_958 = db.Column(db.Integer)
    BB_959 = db.Column(db.Integer)
    BB_960 = db.Column(db.Integer)
    BB_961 = db.Column(db.Integer)
    BB_962 = db.Column(db.Integer)
    BB_963 = db.Column(db.Integer)
    BB_964 = db.Column(db.Integer)
    BB_966 = db.Column(db.Integer)
    BB_967 = db.Column(db.Integer)
    BB_968 = db.Column(db.Integer)
    BB_969 = db.Column(db.Integer)
    BB_970 = db.Column(db.Integer)
    BB_971 = db.Column(db.Integer)
    BB_972 = db.Column(db.Integer)
    BB_973 = db.Column(db.Integer)
    BB_974 = db.Column(db.Integer)
    BB_975 = db.Column(db.Integer)
    BB_978 = db.Column(db.Integer)
    BB_1233 = db.Column(db.Integer)
    BB_1234 = db.Column(db.Integer)
    BB_1235 = db.Column(db.Integer)
    BB_1236 = db.Column(db.Integer)
    BB_1237 = db.Column(db.Integer)
    BB_1238 = db.Column(db.Integer)
    BB_1242 = db.Column(db.Integer)
    BB_1243 = db.Column(db.Integer)
    BB_1246 = db.Column(db.Integer)
    BB_1253 = db.Column(db.Integer)
    BB_1254 = db.Column(db.Integer)
    BB_1258 = db.Column(db.Integer)
    BB_1259 = db.Column(db.Integer)
    BB_1260 = db.Column(db.Integer)
    BB_1264 = db.Column(db.Integer)
    BB_1265 = db.Column(db.Integer)
    BB_1273 = db.Column(db.Integer)
    BB_1275 = db.Column(db.Integer)
    BB_1276 = db.Column(db.Integer)
    BB_1277 = db.Column(db.Integer)
    BB_1278 = db.Column(db.Integer)
    BB_1279 = db.Column(db.Integer)
    BB_1280 = db.Column(db.Integer)
    BB_1281 = db.Column(db.Integer)
    BB_1282 = db.Column(db.Integer)
    BB_1283 = db.Column(db.Integer)
    BB_1284 = db.Column(db.Integer)
    BB_1285 = db.Column(db.Integer)
    BB_1286 = db.Column(db.Integer)
    BB_1287 = db.Column(db.Integer)
    BB_1288 = db.Column(db.Integer)
    BB_1289 = db.Column(db.Integer)
    BB_1290 = db.Column(db.Integer)
    BB_1291 = db.Column(db.Integer)
    BB_1292 = db.Column(db.Integer)
    BB_1293 = db.Column(db.Integer)
    BB_1294 = db.Column(db.Integer)
    BB_1295 = db.Column(db.Integer)
    BB_1296 = db.Column(db.Integer)
    BB_1297 = db.Column(db.Integer)
    BB_1298 = db.Column(db.Integer)
    BB_1308 = db.Column(db.Integer)
    BB_1309 = db.Column(db.Integer)
    BB_1310 = db.Column(db.Integer)
    BB_1374 = db.Column(db.Integer)
    BB_1415 = db.Column(db.Integer)
    BB_1439 = db.Column(db.Integer)
    BB_1441 = db.Column(db.Integer)
    BB_1443 = db.Column(db.Integer)
    BB_1486 = db.Column(db.Integer)
    BB_1487 = db.Column(db.Integer)
    BB_1489 = db.Column(db.Integer)
    BB_1490 = db.Column(db.Integer)
    BB_1491 = db.Column(db.Integer)
    BB_1494 = db.Column(db.Integer)
    BB_1495 = db.Column(db.Integer)
    BB_1497 = db.Column(db.Integer)
    BB_1499 = db.Column(db.Integer)
    BB_1500 = db.Column(db.Integer)
    BB_1501 = db.Column(db.Integer)
    BB_1502 = db.Column(db.Integer)
    BB_1503 = db.Column(db.Integer)
    BB_1504 = db.Column(db.Integer)
    BB_1505 = db.Column(db.Integer)
    BB_1506 = db.Column(db.Integer)
    BB_1507 = db.Column(db.Integer)
    BB_1508 = db.Column(db.Integer)
    BB_1510 = db.Column(db.Integer)
    BB_1511 = db.Column(db.Integer)
    BB_1512 = db.Column(db.Integer)
    BB_1513 = db.Column(db.Integer)
    BB_1514 = db.Column(db.Integer)
    BB_1515 = db.Column(db.Integer)
    BB_1516 = db.Column(db.Integer)
    BB_1517 = db.Column(db.Integer)
    BB_1518 = db.Column(db.Integer)
    BB_1519 = db.Column(db.Integer)
    BB_1521 = db.Column(db.Integer)
    BB_1524 = db.Column(db.Integer)
    BB_1526 = db.Column(db.Integer)
    BB_1527 = db.Column(db.Integer)
    BB_1530 = db.Column(db.Integer)
    BB_1531 = db.Column(db.Integer)
    BB_1532 = db.Column(db.Integer)
    BB_1533 = db.Column(db.Integer)
    BB_1534 = db.Column(db.Integer)
    BB_1535 = db.Column(db.Integer)
    BB_1536 = db.Column(db.Integer)
    BB_1537 = db.Column(db.Integer)
    BB_1539 = db.Column(db.Integer)
    BB_1540 = db.Column(db.Integer)
    BB_1541 = db.Column(db.Integer)
    BB_1542 = db.Column(db.Integer)
    BB_1543 = db.Column(db.Integer)
    BB_1544 = db.Column(db.Integer)
    BB_1545 = db.Column(db.Integer)
    BB_1546 = db.Column(db.Integer)
    BB_1547 = db.Column(db.Integer)
    BB_1548 = db.Column(db.Integer)
    BB_1549 = db.Column(db.Integer)
    BB_1550 = db.Column(db.Integer)
    BB_1551 = db.Column(db.Integer)
    BB_1552 = db.Column(db.Integer)
    BB_1553 = db.Column(db.Integer)
    BB_1554 = db.Column(db.Integer)
    BB_1555 = db.Column(db.Integer)
    BB_1556 = db.Column(db.Integer)
    BB_1557 = db.Column(db.Integer)
    BB_1558 = db.Column(db.Integer)
    BB_1561 = db.Column(db.Integer)
    BB_1562 = db.Column(db.Integer)
    BB_1563 = db.Column(db.Integer)
    BB_1564 = db.Column(db.Integer)
    BB_1572 = db.Column(db.Integer)
    BB_1573 = db.Column(db.Integer)
    BB_1574 = db.Column(db.Integer)
    BB_1576 = db.Column(db.Integer)
    BB_1577 = db.Column(db.Integer)
    BB_1581 = db.Column(db.Integer)
    BB_1601 = db.Column(db.Integer)
    
    def __repr__(self):
        return f"OTU: {self.otu_id}"

# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()

#################################################
# Flask Routes
#################################################
@app.route("/")
def init():
    """Render Home Page."""
    return render_template("index.html")

@app.route('/names')
def get_names():

    results = db.session.query(Metadata.sampleid)
    names = []
    for r in results:
        names.append(r.sampleid)
    return jsonify(names)

    """ Returns a list of sample names in the format
    [
        "BB_940",
        "BB_941",
        ...
    ]
    """

@app.route('/otu')
def otu():
    
    results = db.session.query(Otu.lowest_taxonomic_unit_found)
    otu_descriptions = []
    for r in results:
        otu_descriptions.append(r.lowest_taxonomic_unit_found)
    return jsonify(otu_descriptions)

    """ Returns a list of OTU descriptions in the following format
    [
        "Archaea;Euryarchaeota;Halobacteria;Halococcus",
        "Bacteria",
        ...
    ]
    """

@app.route('/metadata/<sample>')
def sample_metadata(sample):    
    
    results = db.session.query(Metadata.sampleid, 
                                Metadata.age, 
                                Metadata.bbtype,
                                Metadata.ethnicity,
                                Metadata.gender,
                                Metadata.location).all()

    sample_result = {}

    for r in results:
        if r.sampleid == sample:
            sample_result["AGE"] = r.age
            sample_result["BBTYPE"] = r.bbtype
            sample_result["ETHNICITY"] = r.ethnicity
            sample_result["GENDER"] = r.gender
            sample_result["LOCATION"] = r.location
            sample_result["SAMPLEID"] = r.sampleid
    
    return jsonify(sample_result)

    
    """Args: Sample in the format: `BB_940`

    Returns a json dictionary of sample metadata in the format

    {
        AGE: 24,
        BBTYPE: "I",
        ETHNICITY: "Caucasian",
        GENDER: "F",
        LOCATION: "Beaufort/NC",
        SAMPLEID: 940
    }
    """

@app.route('/wfreq/<sample>')
def wfreq_sample(sample):

    results = db.session.query(Metadata.sampleid, Metadata.wfreq)

    for r in results:
        if r.sampleid == sample:
            return jsonify(r.wfreq)

    
    """Args: Sample in the format: `BB_940`

    Returns an integer value for the weekly washing frequency `WFREQ`
    """

@app.route('/samples/<sample>')
def otu_sample(sample):

    column_list = ['otu_id',
                    'BB_940',
                    'BB_941',
                    'BB_943',
                    'BB_944',
                    'BB_945',
                    'BB_946',
                    'BB_947',
                    'BB_948',
                    'BB_949',
                    'BB_950',
                    'BB_952',
                    'BB_953',
                    'BB_954',
                    'BB_955',
                    'BB_956',
                    'BB_958',
                    'BB_959',
                    'BB_960',
                    'BB_961',
                    'BB_962',
                    'BB_963',
                    'BB_964',
                    'BB_966',
                    'BB_967',
                    'BB_968',
                    'BB_969',
                    'BB_970',
                    'BB_971',
                    'BB_972',
                    'BB_973',
                    'BB_974',
                    'BB_975',
                    'BB_978',
                    'BB_1233',
                    'BB_1234',
                    'BB_1235',
                    'BB_1236',
                    'BB_1237',
                    'BB_1238',
                    'BB_1242',
                    'BB_1243',
                    'BB_1246',
                    'BB_1253',
                    'BB_1254',
                    'BB_1258',
                    'BB_1259',
                    'BB_1260',
                    'BB_1264',
                    'BB_1265',
                    'BB_1273',
                    'BB_1275',
                    'BB_1276',
                    'BB_1277',
                    'BB_1278',
                    'BB_1279',
                    'BB_1280',
                    'BB_1281',
                    'BB_1282',
                    'BB_1283',
                    'BB_1284',
                    'BB_1285',
                    'BB_1286',
                    'BB_1287',
                    'BB_1288',
                    'BB_1289',
                    'BB_1290',
                    'BB_1291',
                    'BB_1292',
                    'BB_1293',
                    'BB_1294',
                    'BB_1295',
                    'BB_1296',
                    'BB_1297',
                    'BB_1298',
                    'BB_1308',
                    'BB_1309',
                    'BB_1310',
                    'BB_1374',
                    'BB_1415',
                    'BB_1439',
                    'BB_1441',
                    'BB_1443',
                    'BB_1486',
                    'BB_1487',
                    'BB_1489',
                    'BB_1490',
                    'BB_1491',
                    'BB_1494',
                    'BB_1495',
                    'BB_1497',
                    'BB_1499',
                    'BB_1500',
                    'BB_1501',
                    'BB_1502',
                    'BB_1503',
                    'BB_1504',
                    'BB_1505',
                    'BB_1506',
                    'BB_1507',
                    'BB_1508',
                    'BB_1510',
                    'BB_1511',
                    'BB_1512',
                    'BB_1513',
                    'BB_1514',
                    'BB_1515',
                    'BB_1516',
                    'BB_1517',
                    'BB_1518',
                    'BB_1519',
                    'BB_1521',
                    'BB_1524',
                    'BB_1526',
                    'BB_1527',
                    'BB_1530',
                    'BB_1531',
                    'BB_1532',
                    'BB_1533',
                    'BB_1534',
                    'BB_1535',
                    'BB_1536',
                    'BB_1537',
                    'BB_1539',
                    'BB_1540',
                    'BB_1541',
                    'BB_1542',
                    'BB_1543',
                    'BB_1544',
                    'BB_1545',
                    'BB_1546',
                    'BB_1547',
                    'BB_1548',
                    'BB_1549',
                    'BB_1550',
                    'BB_1551',
                    'BB_1552',
                    'BB_1553',
                    'BB_1554',
                    'BB_1555',
                    'BB_1556',
                    'BB_1557',
                    'BB_1558',
                    'BB_1561',
                    'BB_1562',
                    'BB_1563',
                    'BB_1564',
                    'BB_1572',
                    'BB_1573',
                    'BB_1574',
                    'BB_1576',
                    'BB_1577',
                    'BB_1581',
                    'BB_1601']
    for c in column_list:
        if c == sample:
            sample_index = column_list.index(c)

    results = db.session.query(Sample.otu_id,Sample[sample_index]).all()
    results = [r for r in results]
    return jsonify(results)

    """OTU IDs and Sample Values for a given sample.

    Sort your Pandas DataFrame (OTU ID and Sample Value)
    in Descending Order by Sample Value

    Return a list of dictionaries containing sorted lists 
    for `otu_ids` and `sample_values`

    [
        {
            otu_ids: [
                1166,
                2858,
                481,
                ...
            ],
            sample_values: [
                163,
                126,
                113,
                ...
            ]
        }
    ]
    """

if __name__ == '__main__':
    app.run(debug=True)