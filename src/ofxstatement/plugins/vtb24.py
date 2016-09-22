from ofxstatement.plugin import Plugin
#from ofxstatement.parser import StatementParser
#from ofxstatement.statement import StatementLine
from ofxstatement import statement
from ofxstatement.parser import CsvStatementParser
import csv




class Vtb24CSVStatementParser(CsvStatementParser):

    delimiter = ';'
    vtb24_fieldnames = ['account', 'date-operation', 'date-processing', 'amount-operation', 'currency-operation',
                        'amount-in-cur-account', 'currency-account', 'description', 'status']
    date_format = '%Y-%m-%d %H:%M:%S'

    mappings = {"date": 1,
                "memo": 7,
                "amount": 5

                }

    vtb24_fieldnames = ['account', 'date-operation', 'date-processing', 'amount-operation', 'currency-operation',
                        'amount-in-cur-account', 'currency-account', 'description', 'status']

    #def __init__(self, filename):
    #    self.filename = filename



    def parse(self):
        """Main entry point for parsers

        super() implementation will call to split_records and parse_record to
        process the file.
        """
        stmt = super(Vtb24CSVStatementParser, self).parse()
        statement.recalculate_balance(stmt)
        return stmt



    def split_records(self):
        """Return iterable object consisting of a line per transaction
        """

        # Убрать лишние строки
        flag = 0
        lines = []
        for line in self.fin:
            if flag:
                if not line in ['\n', '\r\n']:
                    lines.append(line)
            if line.startswith('Номер карты/'): flag = 1

        return csv.reader(lines,delimiter=self.delimiter)

        #return csv.DictReader(lines, delimiter=vtb24_delimiter, fieldnames=vtb24_fieldnames)

        #return []

    def parse_record(self, line):
        """Parse given transaction line and return StatementLine object
        """


        stmt = self.statement
        if self.cur_record==1:
            #stmt.currency=line[6]
            stmt.account_id=line[0].replace('\'','')

        line[5]=line[5].replace(',','.')
        line[7] = line[7].strip()
        # fill statement line according to mappings
        sl = super(Vtb24CSVStatementParser, self).parse_record(line)

        #sl.trntype=
        #sl.trntype = 'DEBIT' if sl.amount > 0 else 'CREDIT'

        # generate transaction id out of available data
        #sl.id = statement.generate_transaction_id(sl)

        return sl


class Vtb24Plugin(Plugin):
    """Sample plugin (for developers only)
    """

    def get_parser(self, filename):
        vtb24_encoding = 'cp1251'
        vtb24_currency = 'RUB'
        f = open(filename, 'r', encoding=vtb24_encoding)
        parser = Vtb24CSVStatementParser(f)
        parser.statement.currency = self.settings.get('currency', vtb24_currency)
        #parser.statement.account_id = '4' #self.settings['account']
        parser.statement.bank_id = self.settings.get('bank', 'Vtb24')
        return parser
        #return Vtb24Parser(filename)

