from django.shortcuts import render
from django.views import View
from django.http import Http404
from django.template import TemplateDoesNotExist
from single_pages.datas.hybe_data import find_data
from single_pages.datas.hybe_data2 import find_data2
from single_pages.datas.hybe_data3 import find_data3
from single_pages.datas.hybe_data4 import find_data4
from single_pages.datas.hybe_data5 import find_data5
from single_pages.datas.menu_data import find_menu
from data.views import get_data
import json
import os
from free_board.models import Post



class landing(View):
    
    def pie_chart(data):
        label = list(data.keys())[:2]
        chart_data = []
        for i in range(3):
            d = [data[key][i] for key in label]
            chart_data.append(d)
        
        return label, chart_data

    def extract_for_btn(data):
        return list(data.keys())[2]

    def find_datas(id, data):
        if  'Is_' in id:
            Is_data = find_data.find_data('CIS',data)
            Is_label = find_data.find_label()
            return Is_label, Is_data 
        elif 'Fs_' in id:
            if id == 'Fs_Bs':
                Bs_data = find_data.find_BS()
                Bs_label = find_data.find_label()
                return Bs_label, Bs_data
            elif id == 'Fs_Iv':
                Bs_label = find_data.find_label()
                Debt_Ratios_chart_data = landing.pie_chart(find_data.find_Iv.Debt_Ratios())
                Net_Profit_Margin_chart_data = landing.pie_chart(find_data.find_Iv.Net_Profit_Margin())
                Current_Ratio_chart_data = landing.pie_chart(find_data.find_Iv.Current_Ratio())
                Quick_Ratio_chart_data = landing.pie_chart(find_data.find_Iv.Quick_Ratio())
                ROE_chart_data = landing.pie_chart(find_data.find_Iv.ROE())
                btn_list = [
                    landing.extract_for_btn(find_data.find_Iv.Debt_Ratios()),
                    landing.extract_for_btn(find_data.find_Iv.Net_Profit_Margin()),
                    landing.extract_for_btn(find_data.find_Iv.Current_Ratio()),
                    landing.extract_for_btn(find_data.find_Iv.Quick_Ratio()),
                    landing.extract_for_btn(find_data.find_Iv.ROE())
                    ]
                result_data = json.dumps((Bs_label, btn_list , Debt_Ratios_chart_data, Net_Profit_Margin_chart_data, Current_Ratio_chart_data, Quick_Ratio_chart_data, ROE_chart_data))

                return result_data
            else:
                datas = find_data2.find_data()
                Bs_data = [item+'다.' for item in datas.rstrip().split('다.')]
                Bs_data = Bs_data[:-2]
                return Bs_data
        elif 'Bs_' in id:
            if id == 'Bs_Artist':
                Bs_data = find_data3.find_Artist()
                return Bs_data
            else:
                Bs_data = find_data4.find_contract()
                return Bs_data
        elif 'Em_' in id:
            if id == 'Em_Status':
                Bs_data = find_data5.find_htmls('임원및직원등에관한사항')
                return Bs_data
            else:
                Bs_data = find_data5.find_htmls('임원보수')
                return Bs_data
        elif 'board' in id:
            Is_title = ["매출액","매출원가","판매비와관리비","법인세비용(수익)","당기순이익(손실)"]
            Is_data = []
            Is_data.append(find_data.find_data('CIS',"매출액"))
            Is_data.append(find_data.find_data('CIS',"매출원가"))
            Is_data.append(find_data.find_data('CIS',"판매비와관리비"))
            Is_data.append(find_data.find_data('CIS',"법인세비용(수익)"))
            Is_data.append(find_data.find_data('CIS',"당기순이익(손실)"))
            Is_label = find_data.find_label()

            Bs_label = find_data.find_label()
            Debt_Ratios_chart_data = landing.pie_chart(find_data.find_Iv.Debt_Ratios())
            Net_Profit_Margin_chart_data = landing.pie_chart(find_data.find_Iv.Net_Profit_Margin())
            Current_Ratio_chart_data = landing.pie_chart(find_data.find_Iv.Current_Ratio())
            Quick_Ratio_chart_data = landing.pie_chart(find_data.find_Iv.Quick_Ratio())
            ROE_chart_data = landing.pie_chart(find_data.find_Iv.ROE())
            btn_list = [
                landing.extract_for_btn(find_data.find_Iv.Debt_Ratios()),
                landing.extract_for_btn(find_data.find_Iv.Net_Profit_Margin()),
                landing.extract_for_btn(find_data.find_Iv.Current_Ratio()),
                landing.extract_for_btn(find_data.find_Iv.Quick_Ratio()),
                landing.extract_for_btn(find_data.find_Iv.ROE())
                ]
            result_data = json.dumps((Bs_label, btn_list , Debt_Ratios_chart_data, Net_Profit_Margin_chart_data, Current_Ratio_chart_data, Quick_Ratio_chart_data, ROE_chart_data))
            news_list = get_data()[:5]
            recent_posts = Post.objects.order_by('-pk')[:5]
            return Is_label, Is_title, Is_data, result_data, news_list, recent_posts



    def get(self, request):
        # views.py
        self.menu_items = find_menu.find_menu()
        
        try:
            self.dir = request.path.split('/')[-3]
            self.path = request.path.split('/')[-2]
            if self.dir in self.menu_items:
                menu_item = self.menu_items[self.dir]
            else:
                menu_item = None
            menu_dir = self.dir

            load_html = f'single_pages/{self.dir}/{self.path}.html'
            if menu_item:
                for item in menu_item:
                    if item['id'] == self.path:
                        menu_text = item['text']
                        data = landing.find_datas(item['id'], item['key'])
                        print(data)
                    elif item['id'] == 'board':
                        menu_text = item['text']
                        data = landing.find_datas(item['id'], item['key'])
                        print(data)
                return render(request, load_html, {'menu_item': menu_item, 'menu_dir':menu_dir,'menu_text':menu_text, 'datas':data,})
            else:
                return render(request, load_html, {'menu_item': menu_item, 'menu_dir':menu_dir,})
        except TemplateDoesNotExist:
            raise Http404





