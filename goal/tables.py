from .models import Report
from table import Table
from table.columns import Column
from table.utils import A
from table.columns import LinkColumn, Link

class ReportTable(Table):
    id = Column(field='id',header = 'Row Id', attrs={'class': 'custom'}, header_attrs={'width': '10%'})
    worker = Column(field='worker',header = 'Associate', attrs={'title': A('addr')}, header_attrs={'width': '50%'}, sortable = True, searchable = True)
    process = Column(field='process',header = 'process')
    date = Column(field='date',header = 'date')
    count = Column(field='count',header = 'count')
    quality = Column(field='quality',header = 'quality')
    
    class Meta:
        model = Report

class MonthTable(Table):
    worker = Column(field='worker',header = 'worker')
	
    

    class Meta:
        model = Report

    