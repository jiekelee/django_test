import django_tables2 as tables
from .models import fileModel
from django_tables2.utils import A

class fileTable(tables.Table):
    myfile = tables.columns.FileColumn(attrs={'a': {'download': ''}})
    file_delete = tables.LinkColumn('delete',args=[A('id')],text='Delete',verbose_name='opersion')
    class Meta:
        model = fileModel
        template_name = 'django_tables2/bootstrap.html'