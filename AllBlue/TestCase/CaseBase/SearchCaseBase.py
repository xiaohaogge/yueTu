#!/usr/bin/python
 # -*- coding: utf-8 -*-

import json
import random
from AllBlue.TestCase.CaseBase.AllCaseBase import CaseBase
from AllBlue.Common.NightKingSearchResponse import NightKingSearchRes


class SearchBase(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.flag = False


    # todo 对响应状态进行判断；low
    def checkNkStatus(self,nk):
        res = json.loads(nk)
        try:
            res_Status = res['baseResponse']['status']
        except Exception as e:
            raise Exception('nothing error')
        if res_Status == 500:
            self.log.error('status:%s,message:%s' % (res['baseResponse']['status'], res['baseResponse']['message']))
            raise Exception(500)
        elif res_Status == 200:
            if len(res['routing']) == 0:
                self.log.error('status:200,routing信息为null；')
                raise Exception(204)
            else:
                self.log.info('status:200,返回报价无错误；')
        else:
            self.log.error('checkNKStatus: unknow error ')
            raise Exception(404)

    # 定义nightking 的search 是否为200，routing信息是否不为空；
    def checkSearchIsSuccess(self,status=200,**kwargs):
        try:
            if kwargs['baseResponse']['status'] != status:
                return self.log.error("search 报错：%s"%(kwargs['baseResponse']['message']))
            if len(kwargs['routing']) == 0:
                return self.log.warn("routing is null, routing_number=0")
        except Exception as e:
            return self.log.error("search 报错：%s"%e)


    def Test_Currency(self,method=1,env='dev',pro='sscts',cid='ctrip',ori="USD",tar='CNY'):
        '''定义公共方法，用于获取Cuurrncy rate；
            method=1,表示check 是否有获取到汇率，method=2,表示return currency；
        '''
        strJoin = "?providerName={}&cid={}&originalCode={}&targetCode={}".format(pro,cid,ori,tar)
        sendUrl = self.devExchangeRate+strJoin if env=='dev' else self.ProdExchangeRate+strJoin
        # pre-prod-restful-api.gloryholiday.com/nightking/exchangeRate?providerName=sscts&cid=ctrip&originalCode=USD&targetCode=CNY
        resjson = self.sendRequest(method='GET',url=sendUrl)
        resdict = json.loads(resjson)
        if resdict['msg'] == "success":
            self.log.info('获取汇率%s；from:%s to:%s rate:%s' % (resdict['msg'], ori, tar, resdict['exchange_rate']['exchange_rate']))
            print('获取汇率%s；from:%s to:%s rate:%s' % (resdict['msg'], ori, tar, resdict['exchange_rate']['exchange_rate']))
        else:
            return 404
        if method==2:
            return resdict['exchange_rate']['exchange_rate']
        return 200


    def Test_Provider_Master(self,provider='',routings=''):
        '''定义方法，测试从provider 币种到本位币，再到报价币种的测试；'''
        prolist = []
        for d in routings:
            if d["providerName"] == provider:
                prolist.append(d)

        num = len(prolist)
        if num == 0:
            return self.log.info('该供应商没有航线报出:%s'%provider)
        '''随机抽取其中一条航线，进行测试计算；'''
        testnum = random.randint(0,num-1)
        self.log.info('%s总航线数目：%s,选择的是：%s'%(provider,num,testnum))
        testrouting = prolist[testnum]
        proCurrency = testrouting['providerCurrency']
        masCurrency = testrouting['masterCurrency']
        outcurrency = testrouting['currency']
        cuyconversions = testrouting['currencyConversions']
        self.log.info('【2.1.%s是否有获取到provider 到master currency】'%provider )
        pro_res = self.getRoutingCurrencyConvs(method=1,conversions=cuyconversions,
                                         fromC=proCurrency,toC=masCurrency)
        if pro_res:
            self.log.info('汇率转化存在,{}'.format(pro_res))
        else:
            self.log.error('转化汇率不存在；from %s to %s'%(proCurrency,masCurrency))
        # if cid=='iwoflyCOM':
        #     if reqCurrency != 'USD' and reqCurrency !='HKD':
        #         out_res = self.getRoutingCurrencyConvs(method=1,conversions=cuyconversions,
        #                                                fromC=masCurrency,toC=outcurrency)
        #         if out_res:
        #             self.log.info('汇率转化有获取；')
        #         else:
        #             self.log.error('不存在转化汇率；from %s to %s') % (proCurrency, masCurrency)



    def getRoutingCurrencyConvs(self,method=1,conversions=None,fromC='',toC=''):
        '''
        目前提供2种方式：
            1是代码查询是否有这个汇率，返回bool值；
            2是拿取汇率，返回rate，以及source，和policyid
        '''
        if len(conversions)==0:
            self.log.error('conversions is null，big problem；')
            # todo 需要主动抛异常；
        for n in conversions:
            if n['from']==fromC and n['to']==toC:
                if method==1:
                    return True,n['rate']
                if method==2:
                    return n['rate'],n['source'],n['policyId']
        resultFalse = "汇率 from %s to %s nothing"%(fromC,toC)
        return False,resultFalse

    def Test_TargetProviders(self,res):
        case_c2 = NightKingSearchRes(res)
        self.routingslist = case_c2.nkRouting
        for i in case_c2.nkTraceSpans:
            try:
                pro = i['tags']['nk-wb-final-target-providers']
                providers = pro.split(',')
                return providers
            except Exception:
                pass






