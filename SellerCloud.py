from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor
from suds.sax.element import Element

class Sellercloud():

	def __init__(self, Credentials):
		self.Credentials = Credentials
		imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
		imp.filter.add('http://api.sellercloud.com/')
		doctor=ImportDoctor(imp)
		self.cl = Client(self.Credentials['WSDL'], doctor=doctor)
		self.auth = self.cl.factory.create('AuthHeader')
		self.auth.UserName = self.Credentials['UserName']
		self.auth.Password = self.Credentials['Password']
		self.cl.set_options(soapheaders=self.auth)

	def GetClientID(self):
		try: 	result = self.cl.service.GetClientID()
		except:	result = "Error"
		return result

	def ClearCache(self):
		try: 	result = self.cl.service.ClearCache()
		except:	result = "Error"
		return result

	def GetClientID(self):
		try: 	result = self.cl.service.GetClientID()
		except:	result = "Error"
		return result

	def LoadLayouts(self):
		try: 	result = self.cl.service.LoadLayouts()
		except:	result = "Error"
		return result

	def Authenticate(self):
		try: 	result = self.cl.service.Authenticate()
		except:	result = "Error"
		return result

	def GetWarehouses(self):
		try: 	result = self.cl.service.GetWarehouses()
		except:	result = "Error"
		return result

	def Test_Error_EE(self):
		try: 	result = self.cl.service.Test_Error_EE()
		except:	result = "Error"
		return result

	def ClearCacheFull(self):
		try: 	result = self.cl.service.ClearCacheFull()
		except:	result = "Error"
		return result

	def GetSecurityPIN(self):
		try: 	result = self.cl.service.GetSecurityPIN()
		except:	result = "Error"
		return result

	def ListAllCompany(self):
		try: 	result = self.cl.service.ListAllCompany()
		except:	result = "Error"
		return result

	def ListCWAPlugins(self):
		try: 	result = self.cl.service.ListCWAPlugins()
		except:	result = "Error"
		return result

	def Test_Error_SEH(self):
		try: 	result = self.cl.service.Test_Error_SEH()
		except:	result = "Error"
		return result

	def GetPackageTypes(self):
		try: 	result = self.cl.service.GetPackageTypes()
		except:	result = "Error"
		return result

	def GetStandardRoot(self):
		try: 	result = self.cl.service.GetStandardRoot()
		except:	result = "Error"
		return result

	def GetWebImageRoot(self):
		try: 	result = self.cl.service.GetWebImageRoot()
		except:	result = "Error"
		return result

	def ListOrderGroups(self):
		try: 	result = self.cl.service.ListOrderGroups()
		except:	result = "Error"
		return result

	def AsynchronousTest(self):
		try: 	result = self.cl.service.AsynchronousTest()
		except:	result = "Error"
		return result

	def GetClientOptions(self):
		try: 	result = self.cl.service.GetClientOptions()
		except:	result = "Error"
		return result

	def ListAllViewGroups(self):
		try: 	result = self.cl.service.ListAllViewGroups()
		except:	result = "Error"
		return result

	def ListProductGroups(self):
		try: 	result = self.cl.service.ListProductGroups()
		except:	result = "Error"
		return result

	def GetAllPaymentTerms(self):
		try: 	result = self.cl.service.GetAllPaymentTerms()
		except:	result = "Error"
		return result

	def GetSecurityOptions(self):
		try: 	result = self.cl.service.GetSecurityOptions()
		except:	result = "Error"
		return result

	def GetUserInformation(self):
		try: 	result = self.cl.service.GetUserInformation()
		except:	result = "Error"
		return result

	def PickList_CreateNew(self):
		try: 	result = self.cl.service.PickList_CreateNew()
		except:	result = "Error"
		return result

	def GetAllCustomColumns(self):
		try: 	result = self.cl.service.GetAllCustomColumns()
		except:	result = "Error"
		return result

	def POItemStatus_GetAll(self):
		try: 	result = self.cl.service.POItemStatus_GetAll()
		except:	result = "Error"
		return result

	def GetClientSettingsAll(self):
		try: 	result = self.cl.service.GetClientSettingsAll()
		except:	result = "Error"
		return result

	def GeteBayDescImageRoot(self):
		try: 	result = self.cl.service.GeteBayDescImageRoot()
		except:	result = "Error"
		return result

	def GetProductConditions(self):
		try: 	result = self.cl.service.GetProductConditions()
		except:	result = "Error"
		return result

	def ListAllSavedSearches(self):
		try: 	result = self.cl.service.ListAllSavedSearches()
		except:	result = "Error"
		return result

	def PO_GetNewOrderNumber(self):
		try: 	result = self.cl.service.PO_GetNewOrderNumber()
		except:	result = "Error"
		return result

	def ListAllVendorsCurrent(self):
		try: 	result = self.cl.service.ListAllVendorsCurrent()
		except:	result = "Error"
		return result

	def GetAssociatedCompanies(self):
		try: 	result = self.cl.service.GetAssociatedCompanies()
		except:	result = "Error"
		return result

	def ListAllStationsCurrent(self):
		try: 	result = self.cl.service.ListAllStationsCurrent()
		except:	result = "Error"
		return result

	def GetDefaultProductTypeID(self):
		try: 	result = self.cl.service.GetDefaultProductTypeID()
		except:	result = "Error"
		return result

	def ListAllLocationsCurrent(self):
		try: 	result = self.cl.service.ListAllLocationsCurrent()
		except:	result = "Error"
		return result

	def ListOrderInvoicePlugins(self):
		try: 	result = self.cl.service.ListOrderInvoicePlugins()
		except:	result = "Error"
		return result

	def Orders_GetFilterOptions(self):
		try: 	result = self.cl.service.Orders_GetFilterOptions()
		except:	result = "Error"
		return result

	def Orders_GetShippingRules(self):
		try: 	result = self.cl.service.Orders_GetShippingRules()
		except:	result = "Error"
		return result

	def GetBulkUpdateLastSuccess(self):
		try: 	result = self.cl.service.GetBulkUpdateLastSuccess()
		except:	result = "Error"
		return result

	def GetSupplementImagesToFix(self):
		try: 	result = self.cl.service.GetSupplementImagesToFix()
		except:	result = "Error"
		return result

	def PurchaseOrderType_GetAll(self):
		try: 	result = self.cl.service.PurchaseOrderType_GetAll()
		except:	result = "Error"
		return result

	def MultipleWarehousesEnabled(self):
		try: 	result = self.cl.service.MultipleWarehousesEnabled()
		except:	result = "Error"
		return result

	def GetCurrentAmazonMerchantID(self):
		try: 	result = self.cl.service.GetCurrentAmazonMerchantID()
		except:	result = "Error"
		return result

	def Orders_GetAllCacheableData(self):
		try: 	result = self.cl.service.Orders_GetAllCacheableData()
		except:	result = "Error"
		return result

	def PurchaseOrderStatus_GetAll(self):
		try: 	result = self.cl.service.PurchaseOrderStatus_GetAll()
		except:	result = "Error"
		return result

	def SavedSearches_GetAll_Order(self):
		try: 	result = self.cl.service.SavedSearches_GetAll_Order()
		except:	result = "Error"
		return result

	def PurchaseOrderItemStatus_GetAll(self):
		try: 	result = self.cl.service.PurchaseOrderItemStatus_GetAll()
		except:	result = "Error"
		return result

	def WarehouseCartCodesAllforClient(self):
		try: 	result = self.cl.service.WarehouseCartCodesAllforClient()
		except:	result = "Error"
		return result

	def Labels_ListLocationNotesPlugins(self):
		try: 	result = self.cl.service.Labels_ListLocationNotesPlugins()
		except:	result = "Error"
		return result

	def PurchaseOrder_GetNewOrderNumber(self):
		try: 	result = self.cl.service.PurchaseOrder_GetNewOrderNumber()
		except:	result = "Error"
		return result

	def Orders_GetFilterOptions_Advanced(self):
		try: 	result = self.cl.service.Orders_GetFilterOptions_Advanced()
		except:	result = "Error"
		return result

	def ClientSettings_EnableWarehouseBins(self):
		try: 	result = self.cl.service.ClientSettings_EnableWarehouseBins()
		except:	result = "Error"
		return result

	def GetGalleryAndMainDescProductImages(self):
		try: 	result = self.cl.service.GetGalleryAndMainDescProductImages()
		except:	result = "Error"
		return result

	def PhysicalInventoryAdjustment_GetAll(self):
		try: 	result = self.cl.service.PhysicalInventoryAdjustment_GetAll()
		except:	result = "Error"
		return result

	def Orders_GetSupportsShippingConfirmation(self):
		try: 	result = self.cl.service.Orders_GetSupportsShippingConfirmation()
		except:	result = "Error"
		return result

	def QueuedJobs_ExportOrdersToPDFViaPlugin_GetOptions(self):
		try: 	result = self.cl.service.QueuedJobs_ExportOrdersToPDFViaPlugin_GetOptions()
		except:	result = "Error"
		return result

	def GetClientName(self, ClientID):
		try:
			result = self.cl.service.GetClientName(ClientID)
		except:
			result = "Error"
		return result

	def GetClientOptions(self):
		try:
			result = self.cl.service.GetClientOptions()
		except:
			result = "Error"
		return result

	def Product_UpdatePriceOnChannel(self,ProductSetList):
		try:
			for ProductSet in ProductSetList:
				products = self.cl.factory.create('ArrayOfString')
				products.string = ProductSet['ProductID']
				result = self.cl.service.Product_UpdatePriceOnChannel(products, ProductSet['SalesChannel'])
		except:
			result ="Error"
		return result

	def ProductLocation_RemoveQuantitiesOfAnAdjustment(self, adjustmentID):
		try: 	result = self.cl.service.ProductLocation_RemoveQuantitiesOfAnAdjustment(adjustmentID)
		except:	result = "Error"
		return result

	def GetAmazonMerchantCached(self, AmazonCompanyID):
		try: 	result = self.cl.service.GetAmazonMerchantCached(AmazonCompanyID)
		except:	result = "Error"
		return result

	def GetAmazonMerchantCached(self, AmazonCompanyID):
		try: 	result = self.cl.service.GetAmazonMerchantCached(AmazonCompanyID)
		except:	result = "Error"
		return result

	def ShippingLabel_GetPackageTypes(self, CarrierCode):
		try: 	result = self.cl.service.ShippingLabel_GetPackageTypes(CarrierCode)
		except:	result = "Error"
		return result

	def ShippingLabel_GetServices(self, CarrierCode):
		try: 	result = self.cl.service.ShippingLabel_GetServices(CarrierCode)
		except:	result = "Error"
		return result

	def GetRelatedBundles(self, ChildProductID):
		try: 	result = self.cl.service.GetRelatedBundles(ChildProductID)
		except:	result = "Error"
		return result

	def GetRelatedBundles_Simple(self, ChildProductID):
		try: 	result = self.cl.service.GetRelatedBundles_Simple(ChildProductID)
		except:	result = "Error"
		return result

	def GetClientName(self, ClientID):
		try: 	result = self.cl.service.GetClientName(ClientID)
		except:	result = "Error"
		return result

	def GetSettlementDetailsToExportToQuickBooks(self, ClientID):
		try: 	result = self.cl.service.GetSettlementDetailsToExportToQuickBooks(ClientID)
		except:	result = "Error"
		return result

	def GetSettlementFeesByCompanyAndChannel(self, ClientID):
		try: 	result = self.cl.service.GetSettlementFeesByCompanyAndChannel(ClientID)
		except:	result = "Error"
		return result

	def GetSettlementsForExportToQuickBooks(self, ClientID):
		try: 	result = self.cl.service.GetSettlementsForExportToQuickBooks(ClientID)
		except:	result = "Error"
		return result

	def ListAllLocations(self, ClientID):
		try: 	result = self.cl.service.ListAllLocations(ClientID)
		except:	result = "Error"
		return result

	def ListAllStations(self, ClientID):
		try: 	result = self.cl.service.ListAllStations(ClientID)
		except:	result = "Error"
		return result

	def QB_JE_GetChannels(self, ClientID):
		try: 	result = self.cl.service.QB_JE_GetChannels(ClientID)
		except:	result = "Error"
		return result

	def QB_JE_GetCompanies(self, ClientID):
		try: 	result = self.cl.service.QB_JE_GetCompanies(ClientID)
		except:	result = "Error"
		return result

	def QB_JE_GetSettlementDetailsToExportToQuickBooks(self, ClientID):
		try: 	result = self.cl.service.QB_JE_GetSettlementDetailsToExportToQuickBooks(ClientID)
		except:	result = "Error"
		return result

	def QB_JE_GetSettlementFeesByCompanyAndChannel(self, ClientID):
		try: 	result = self.cl.service.QB_JE_GetSettlementFeesByCompanyAndChannel(ClientID)
		except:	result = "Error"
		return result

	def ListAllVendors(self, CompanyID):
		try: 	result = self.cl.service.ListAllVendors(CompanyID)
		except:	result = "Error"
		return result

	def ListProductsForInventoryExportForWebSite(self, CompanyID):
		try: 	result = self.cl.service.ListProductsForInventoryExportForWebSite(CompanyID)
		except:	result = "Error"
		return result

	def ListProductType(self, CompanyID):
		try: 	result = self.cl.service.ListProductType(CompanyID)
		except:	result = "Error"
		return result

	def Manufacturer_ListALL(self, CompanyID):
		try: 	result = self.cl.service.Manufacturer_ListALL(CompanyID)
		except:	result = "Error"
		return result

	def Orders_GetCancelledOrdersToExport(self, CompanyID):
		try: 	result = self.cl.service.Orders_GetCancelledOrdersToExport(CompanyID)
		except:	result = "Error"
		return result

	def Orders_GetOrdersToExport(self, CompanyID):
		try: 	result = self.cl.service.Orders_GetOrdersToExport(CompanyID)
		except:	result = "Error"
		return result

	def Repricing_ListAllRules(self, CompanyID):
		try: 	result = self.cl.service.Repricing_ListAllRules(CompanyID)
		except:	result = "Error"
		return result

	def Vendors_ListALL(self, CompanyID):
		try: 	result = self.cl.service.Vendors_ListALL(CompanyID)
		except:	result = "Error"
		return result

	def Orders_DeleteDocument(self, DocumentID):
		try: 	result = self.cl.service.Orders_DeleteDocument(DocumentID)
		except:	result = "Error"
		return result

	def Orders_GetDocument(self, DocumentID):
		try: 	result = self.cl.service.Orders_GetDocument(DocumentID)
		except:	result = "Error"
		return result

	def Orders_GetDocumentData(self, DocumentID):
		try: 	result = self.cl.service.Orders_GetDocumentData(DocumentID)
		except:	result = "Error"
		return result

	def GetProductsByEbayItemID(self, eBayItemID):
		try: 	result = self.cl.service.GetProductsByEbayItemID(eBayItemID)
		except:	result = "Error"
		return result

	def PhysicalInventoryAdjustmentItem_Delete(self, ID):
		try: 	result = self.cl.service.PhysicalInventoryAdjustmentItem_Delete(ID)
		except:	result = "Error"
		return result

	def DeleteImage(self, ID):
		try: 	result = self.cl.service.DeleteImage(ID)
		except:	result = "Error"
		return result

	def GetImageDetails(self, ID):
		try: 	result = self.cl.service.GetImageDetails(ID)
		except:	result = "Error"
		return result

	def GetImageInfoDetails(self, ID):
		try: 	result = self.cl.service.GetImageInfoDetails(ID)
		except:	result = "Error"
		return result

	def PhysicalInventoryAdjustment_Get(self, ID):
		try: 	result = self.cl.service.PhysicalInventoryAdjustment_Get(ID)
		except:	result = "Error"
		return result

	def PhysicalInventoryAdjustmentItem_DeleteAllOfAnAdjustment(self, ID):
		try: 	result = self.cl.service.PhysicalInventoryAdjustmentItem_DeleteAllOfAnAdjustment(ID)
		except:	result = "Error"
		return result

	def PhysicalInventoryAdjustmentItem_GetAllOfAnAdjustment(self, ID):
		try: 	result = self.cl.service.PhysicalInventoryAdjustmentItem_GetAllOfAnAdjustment(ID)
		except:	result = "Error"
		return result

	def PickList_GetPickList(self, ID):
		try: 	result = self.cl.service.PickList_GetPickList(ID)
		except:	result = "Error"
		return result

	def PickList_GetPickListInfo(self, ID):
		try: 	result = self.cl.service.PickList_GetPickListInfo(ID)
		except:	result = "Error"
		return result

	def PickList_ListOrdersInPickList(self, ID):
		try: 	result = self.cl.service.PickList_ListOrdersInPickList(ID)
		except:	result = "Error"
		return result

	def PickList_Product_GetProduct(self, ID):
		try: 	result = self.cl.service.PickList_Product_GetProduct(ID)
		except:	result = "Error"
		return result

	def PO_Get(self, ID):
		try: 	result = self.cl.service.PO_Get(ID)
		except:	result = "Error"
		return result

	def POItem_SetDeleted(self, ID):
		try: 	result = self.cl.service.POItem_SetDeleted(ID)
		except:	result = "Error"
		return result

	def PurchaseOrder_Get(self, ID):
		try: 	result = self.cl.service.PurchaseOrder_Get(ID)
		except:	result = "Error"
		return result

	def PurchaseOrderItem_SetDeleted(self, ID):
		try: 	result = self.cl.service.PurchaseOrderItem_SetDeleted(ID)
		except:	result = "Error"
		return result

	def WarehouseInventoryAdjustment_Delete(self, ID):
		try: 	result = self.cl.service.WarehouseInventoryAdjustment_Delete(ID)
		except:	result = "Error"
		return result

	def WarehouseInventoryAdjustment_Get(self, ID):
		try: 	result = self.cl.service.WarehouseInventoryAdjustment_Get(ID)
		except:	result = "Error"
		return result

	def GetBundleItemsSortBySequence(self, ID):
		try: 	result = self.cl.service.GetBundleItemsSortBySequence(ID)
		except:	result = "Error"
		return result

	def GetProduct(self, ID):
		try: 	result = self.cl.service.GetProduct(ID)
		except:	result = "Error"
		return result

	def GetProductAliases(self, ID):
		try: 	result = self.cl.service.GetProductAliases(ID)
		except:	result = "Error"
		return result

	def GetProductInfo(self, ID):
		try: 	result = self.cl.service.GetProductInfo(ID)
		except:	result = "Error"
		return result

	def GetProductReplacementSKUs(self, ID):
		try: 	result = self.cl.service.GetProductReplacementSKUs(ID)
		except:	result = "Error"
		return result

	def GetProductShadows(self, ID):
		try: 	result = self.cl.service.GetProductShadows(ID)
		except:	result = "Error"
		return result

	def GetProductVanilla(self, ID):
		try: 	result = self.cl.service.GetProductVanilla(ID)
		except:	result = "Error"
		return result

	def SetProductBuyDotComPriceUseDefault(self, ID):
		try: 	result = self.cl.service.SetProductBuyDotComPriceUseDefault(ID)
		except:	result = "Error"
		return result

	def SetProductNewEggDotComPriceUseDefault(self, ID):
		try: 	result = self.cl.service.SetProductNewEggDotComPriceUseDefault(ID)
		except:	result = "Error"
		return result

	def GetCompanyImageFromOrderID(self, OrderID):
		try: 	result = self.cl.service.GetCompanyImageFromOrderID(OrderID)
		except:	result = "Error"
		return result

	def GetOrderByID(self, OrderID):
		try: 	result = self.cl.service.GetOrderByID(OrderID)
		except:	result = "Error"
		return result

	def OrderPackages_ListAllForOrder(self, OrderID):
		try: 	result = self.cl.service.OrderPackages_ListAllForOrder(OrderID)
		except:	result = "Error"
		return result

	def Orders_CalculateOrderCost(self, OrderID):
		try: 	result = self.cl.service.Orders_CalculateOrderCost(OrderID)
		except:	result = "Error"
		return result

	def Orders_CalculateOrderItemsCost(self, OrderID):
		try: 	result = self.cl.service.Orders_CalculateOrderItemsCost(OrderID)
		except:	result = "Error"
		return result

	def Orders_DeletePackagesForOrder(self, OrderID):
		try: 	result = self.cl.service.Orders_DeletePackagesForOrder(OrderID)
		except:	result = "Error"
		return result

	def Orders_GeneratePackages(self, OrderID):
		try: 	result = self.cl.service.Orders_GeneratePackages(OrderID)
		except:	result = "Error"
		return result

	def Orders_GetCustomerInstructions(self, OrderID):
		try: 	result = self.cl.service.Orders_GetCustomerInstructions(OrderID)
		except:	result = "Error"
		return result

	def Orders_GetData(self, OrderID):
		try: 	result = self.cl.service.Orders_GetData(OrderID)
		except:	result = "Error"
		return result

	def Orders_GetDownloadedSingle(self, OrderID):
		try: 	result = self.cl.service.Orders_GetDownloadedSingle(OrderID)
		except:	result = "Error"
		return result

	def Orders_GetOrderItemsNeedingSerialScan(self, OrderID):
		try: 	result = self.cl.service.Orders_GetOrderItemsNeedingSerialScan(OrderID)
		except:	result = "Error"
		return result

	def Orders_GetOrderState(self, OrderID):
		try: 	result = self.cl.service.Orders_GetOrderState(OrderID)
		except:	result = "Error"
		return result

	def Orders_GetPDFInvoice(self, OrderID):
		try: 	result = self.cl.service.Orders_GetPDFInvoice(OrderID)
		except:	result = "Error"
		return result

	def Orders_GetRelatedKitsForOrder(self, OrderID):
		try: 	result = self.cl.service.Orders_GetRelatedKitsForOrder(OrderID)
		except:	result = "Error"
		return result

	def Orders_GetShippedVerifiedByOrderNumber(self, OrderID):
		try: 	result = self.cl.service.Orders_GetShippedVerifiedByOrderNumber(OrderID)
		except:	result = "Error"
		return result

	def Orders_ListAllDocuments(self, OrderID):
		try: 	result = self.cl.service.Orders_ListAllDocuments(OrderID)
		except:	result = "Error"
		return result

	def Orders_MarkAsCancelled(self, OrderID):
		try: 	result = self.cl.service.Orders_MarkAsCancelled(OrderID)
		except:	result = "Error"
		return result

	def Orders_NotifyBuyerForOrderShipped(self, OrderID):
		try: 	result = self.cl.service.Orders_NotifyBuyerForOrderShipped(OrderID)
		except:	result = "Error"
		return result

	def Orders_NotifyOrderSourceForOrderShipped(self, OrderID):
		try: 	result = self.cl.service.Orders_NotifyOrderSourceForOrderShipped(OrderID)
		except:	result = "Error"
		return result

	def Orders_UpdateShippedVerifiedByOrderNumber(self, OrderID):
		try: 	result = self.cl.service.Orders_UpdateShippedVerifiedByOrderNumber(OrderID)
		except:	result = "Error"
		return result

	def Orders_UpdateShippedVerifiedByOrderNumberUndo(self, OrderID):
		try: 	result = self.cl.service.Orders_UpdateShippedVerifiedByOrderNumberUndo(OrderID)
		except:	result = "Error"
		return result

	def PickList_IsSingleItemOrder(self, OrderID):
		try: 	result = self.cl.service.PickList_IsSingleItemOrder(OrderID)
		except:	result = "Error"
		return result

	def PickList_Order_IsFullyPicked(self, OrderID):
		try: 	result = self.cl.service.PickList_Order_IsFullyPicked(OrderID)
		except:	result = "Error"
		return result

	def PickLock_Get(self, OrderID):
		try: 	result = self.cl.service.PickLock_Get(OrderID)
		except:	result = "Error"
		return result

	def PickLock_Release(self, OrderID):
		try: 	result = self.cl.service.PickLock_Release(OrderID)
		except:	result = "Error"
		return result

	def Product_GetShippingPreferencesForOrder(self, OrderID):
		try: 	result = self.cl.service.Product_GetShippingPreferencesForOrder(OrderID)
		except:	result = "Error"
		return result

	def RefreshOrder(self, OrderID):
		try: 	result = self.cl.service.RefreshOrder(OrderID)
		except:	result = "Error"
		return result

	def UpdateOrderAsExported(self, OrderID):
		try: 	result = self.cl.service.UpdateOrderAsExported(OrderID)
		except:	result = "Error"
		return result

	def UpdateQtyShipped(self, OrderID):
		try: 	result = self.cl.service.UpdateQtyShipped(OrderID)
		except:	result = "Error"
		return result

	def WarehouseBinOrder_ListBinsByOrderID(self, OrderID):
		try: 	result = self.cl.service.WarehouseBinOrder_ListBinsByOrderID(OrderID)
		except:	result = "Error"
		return result

	def Orders_MarkAsCancelled_By_OrderSourceOrderID(self, OrderSourceOrderID):
		try: 	result = self.cl.service.Orders_MarkAsCancelled_By_OrderSourceOrderID(OrderSourceOrderID)
		except:	result = "Error"
		return result

	def GetGalleryImageURL(self, ProductID):
		try: 	result = self.cl.service.GetGalleryImageURL(ProductID)
		except:	result = "Error"
		return result

	def GetInventoryAvailableQty(self, ProductID):
		try: 	result = self.cl.service.GetInventoryAvailableQty(ProductID)
		except:	result = "Error"
		return result

	def GetKitInfo(self, ProductID):
		try: 	result = self.cl.service.GetKitInfo(ProductID)
		except:	result = "Error"
		return result

	def GetKitWeight(self, ProductID):
		try: 	result = self.cl.service.GetKitWeight(ProductID)
		except:	result = "Error"
		return result

	def GetProductAttributes(self, ProductID):
		try: 	result = self.cl.service.GetProductAttributes(ProductID)
		except:	result = "Error"
		return result

	def GetProductDimensions(self, ProductID):
		try: 	result = self.cl.service.GetProductDimensions(ProductID)
		except:	result = "Error"
		return result

	def GetProductEditDynamicInfo(self, ProductID):
		try: 	result = self.cl.service.GetProductEditDynamicInfo(ProductID)
		except:	result = "Error"
		return result

	def GetProductEditInfo(self, ProductID):
		try: 	result = self.cl.service.GetProductEditInfo(ProductID)
		except:	result = "Error"
		return result

	def GetProductFullInfo(self, ProductID):
		try: 	result = self.cl.service.GetProductFullInfo(ProductID)
		except:	result = "Error"
		return result

	def GetProductGroupsForProductID(self, ProductID):
		try: 	result = self.cl.service.GetProductGroupsForProductID(ProductID)
		except:	result = "Error"
		return result

	def GetProductInventoryForALLWarehouses(self, ProductID):
		try: 	result = self.cl.service.GetProductInventoryForALLWarehouses(ProductID)
		except:	result = "Error"
		return result

	def GetProductUnShippedCommittedQty(self, ProductID):
		try: 	result = self.cl.service.GetProductUnShippedCommittedQty(ProductID)
		except:	result = "Error"
		return result

	def ListProductImageInfo(self, ProductID):
		try: 	result = self.cl.service.ListProductImageInfo(ProductID)
		except:	result = "Error"
		return result

	def ListProductImages(self, ProductID):
		try: 	result = self.cl.service.ListProductImages(ProductID)
		except:	result = "Error"
		return result

	def LoadProduct(self, ProductID):
		try: 	result = self.cl.service.LoadProduct(ProductID)
		except:	result = "Error"
		return result

	def Orders_GetProductProductWeight(self, ProductID):
		try: 	result = self.cl.service.Orders_GetProductProductWeight(ProductID)
		except:	result = "Error"
		return result

	def Orders_GetProductShipWeight(self, ProductID):
		try: 	result = self.cl.service.Orders_GetProductShipWeight(ProductID)
		except:	result = "Error"
		return result

	def ProduceReplacement_ListALL(self, ProductID):
		try: 	result = self.cl.service.ProduceReplacement_ListALL(ProductID)
		except:	result = "Error"
		return result

	def Product_Delete(self, ProductID):
		try: 	result = self.cl.service.Product_Delete(ProductID)
		except:	result = "Error"
		return result

	def Product_GetWebSiteCategories(self, ProductID):
		try: 	result = self.cl.service.Product_GetWebSiteCategories(ProductID)
		except:	result = "Error"
		return result

	def Product_IsMatrixParent(self, ProductID):
		try: 	result = self.cl.service.Product_IsMatrixParent(ProductID)
		except:	result = "Error"
		return result

	def ProductLocation_GetAllOfProduct(self, ProductID):
		try: 	result = self.cl.service.ProductLocation_GetAllOfProduct(ProductID)
		except:	result = "Error"
		return result

	def ProductRebate_GetAllForProduct(self, ProductID):
		try: 	result = self.cl.service.ProductRebate_GetAllForProduct(ProductID)
		except:	result = "Error"
		return result

	def Products_SerialNumber_DeleteAll(self, ProductID):
		try: 	result = self.cl.service.Products_SerialNumber_DeleteAll(ProductID)
		except:	result = "Error"
		return result

	def Products_SerialNumber_ListAll(self, ProductID):
		try: 	result = self.cl.service.Products_SerialNumber_ListAll(ProductID)
		except:	result = "Error"
		return result

	def ReplacementPair_GetReplacementWithMaxQty(self, ProductID):
		try: 	result = self.cl.service.ReplacementPair_GetReplacementWithMaxQty(ProductID)
		except:	result = "Error"
		return result

	def Replacements_GetReplacementWithMaxQty(self, ProductID):
		try: 	result = self.cl.service.Replacements_GetReplacementWithMaxQty(ProductID)
		except:	result = "Error"
		return result

	def WarehouseInventoryAdjustment_ListAll(self, ProductID):
		try: 	result = self.cl.service.WarehouseInventoryAdjustment_ListAll(ProductID)
		except:	result = "Error"
		return result

	def GetProductsByUPC(self, UPC):
		try: 	result = self.cl.service.GetProductsByUPC(UPC)
		except:	result = "Error"
		return result

	def GetUser(self, UserID):
		try: 	result = self.cl.service.GetUser(UserID)
		except:	result = "Error"
		return result

	def GetUserByID(self, UserID):
		try: 	result = self.cl.service.GetUserByID(UserID)
		except:	result = "Error"
		return result

	def Vendors_GetVendor(self, VendorID):
		try: 	result = self.cl.service.Vendors_GetVendor(VendorID)
		except:	result = "Error"
		return result

	def GetCurrentUserInfo(self, WarehouseID):
		try: 	result = self.cl.service.GetCurrentUserInfo(WarehouseID)
		except:	result = "Error"
		return result

	def GetWarehouseFromID(self, WarehouseID):
		try: 	result = self.cl.service.GetWarehouseFromID(WarehouseID)
		except:	result = "Error"
		return result

	def WarehouseBin_GetDisAssembleBin(self, WarehouseID):
		try: 	result = self.cl.service.WarehouseBin_GetDisAssembleBin(WarehouseID)
		except:	result = "Error"
		return result

	def WarehouseBin_GetInterimBin(self, WarehouseID):
		try: 	result = self.cl.service.WarehouseBin_GetInterimBin(WarehouseID)
		except:	result = "Error"
		return result

	def WarehouseBin_GetPickingBin(self, WarehouseID):
		try: 	result = self.cl.service.WarehouseBin_GetPickingBin(WarehouseID)
		except:	result = "Error"
		return result

	def WarehouseBin_GetPickingBin_FBA(self, WarehouseID):
		try: 	result = self.cl.service.WarehouseBin_GetPickingBin_FBA(WarehouseID)
		except:	result = "Error"
		return result

	def WarehouseBin_GetPickingBin_W2W(self, WarehouseID):
		try: 	result = self.cl.service.WarehouseBin_GetPickingBin_W2W(WarehouseID)
		except:	result = "Error"
		return result

	def WarehouseBin_GetReceivingBin(self, WarehouseID):
		try: 	result = self.cl.service.WarehouseBin_GetReceivingBin(WarehouseID)
		except:	result = "Error"
		return result

	def WarehouseBin_GetTempBin(self, WarehouseID):
		try: 	result = self.cl.service.WarehouseBin_GetTempBin(WarehouseID)
		except:	result = "Error"
		return result

	def WarehouseBin_PrimaryNeedRefilled(self, WarehouseID):
		try: 	result = self.cl.service.WarehouseBin_PrimaryNeedRefilled(WarehouseID)
		except:	result = "Error"
		return result

	def AmazonCube_SaveProductSummary(self, ASIN):
		try: 	result = self.cl.service.AmazonCube_SaveProductSummary(ASIN)
		except:	result = "Error"
		return result

	def GetAllWebSiteCategories(self, CompanyID):
		try: 	result = self.cl.service.GetAllWebSiteCategories(CompanyID)
		except:	result = "Error"
		return result

	def GetAmazonMerchant(self, CompanyID):
		try: 	result = self.cl.service.GetAmazonMerchant(CompanyID)
		except:	result = "Error"
		return result

	def GetCompany(self, CompanyID):
		try: 	result = self.cl.service.GetCompany(CompanyID)
		except:	result = "Error"
		return result

	def GetCompanyImage(self, CompanyID):
		try: 	result = self.cl.service.GetCompanyImage(CompanyID)
		except:	result = "Error"
		return result

	def GetCompanyLogo(self, CompanyID):
		try: 	result = self.cl.service.GetCompanyLogo(CompanyID)
		except:	result = "Error"
		return result

	def BulkUpdateCleanUp(self, companyIDToClean):
		try: 	result = self.cl.service.BulkUpdateCleanUp(companyIDToClean)
		except:	result = "Error"
		return result

	def AmazonCube_RepricingDataSummary(self, ProductID):
		try: 	result = self.cl.service.AmazonCube_RepricingDataSummary(ProductID)
		except:	result = "Error"
		return result

	def WarehouseBin_AllInBin(self, BinID):
		try: 	result = self.cl.service.WarehouseBin_AllInBin(BinID)
		except:	result = "Error"
		return result

	def WarehouseBin_Get(self, BinID):
		try: 	result = self.cl.service.WarehouseBin_Get(BinID)
		except:	result = "Error"
		return result

	def WarehouseBinOrder_ListOrdersByBinID(self, BinID):
		try: 	result = self.cl.service.WarehouseBinOrder_ListOrdersByBinID(BinID)
		except:	result = "Error"
		return result

	def BulkUpdateFieldsKits(self, contents):
		try: 	result = self.cl.service.BulkUpdateFieldsKits(contents)
		except:	result = "Error"
		return result

	def BulkUpdateFieldsKitsQueue(self, contents):
		try: 	result = self.cl.service.BulkUpdateFieldsKitsQueue(contents)
		except:	result = "Error"
		return result

	def BulkUpdateFieldsShadows(self, contents):
		try: 	result = self.cl.service.BulkUpdateFieldsShadows(contents)
		except:	result = "Error"
		return result

	def BulkUpdateFieldsShadowsQueue(self, contents):
		try: 	result = self.cl.service.BulkUpdateFieldsShadowsQueue(contents)
		except:	result = "Error"
		return result

	def GetClientSettingsAllForClientID(self, CustomClientID):
		try: 	result = self.cl.service.GetClientSettingsAllForClientID(CustomClientID)
		except:	result = "Error"
		return result

	def GetSupportsFeature(self, feature):
		try: 	result = self.cl.service.GetSupportsFeature(feature)
		except:	result = "Error"
		return result

	def BulkUpdate_DownloadFile(self, fileID):
		try: 	result = self.cl.service.BulkUpdate_DownloadFile(fileID)
		except:	result = "Error"
		return result

	def ListAllViewGroupItems(self, GroupId):
		try: 	result = self.cl.service.ListAllViewGroupItems(GroupId)
		except:	result = "Error"
		return result

	def QueuedJobs_EnableNotesOnClientLevel(self, jobID):
		try: 	result = self.cl.service.QueuedJobs_EnableNotesOnClientLevel(jobID)
		except:	result = "Error"
		return result

	def QueuedJobs_GetErrors(self, jobID):
		try: 	result = self.cl.service.QueuedJobs_GetErrors(jobID)
		except:	result = "Error"
		return result

	def QueuedJobs_GetJob(self, jobID):
		try: 	result = self.cl.service.QueuedJobs_GetJob(jobID)
		except:	result = "Error"
		return result

	def QueuedJobs_GetOutputFile(self, jobID):
		try: 	result = self.cl.service.QueuedJobs_GetOutputFile(jobID)
		except:	result = "Error"
		return result

	def QueuedJobs_GetStatus(self, jobID):
		try: 	result = self.cl.service.QueuedJobs_GetStatus(jobID)
		except:	result = "Error"
		return result

	def SearchProductsWithASIN(self, keywords):
		try: 	result = self.cl.service.SearchProductsWithASIN(keywords)
		except:	result = "Error"
		return result

	def SearchProducts(self, keywords):
		try: 	result = self.cl.service.SearchProducts(keywords)
		except:	result = "Error"
		return result

	def ProductKit_GetKitDetails(self, KitParentProductID):
		try: 	result = self.cl.service.ProductKit_GetKitDetails(KitParentProductID)
		except:	result = "Error"
		return result

	def GetWarehouseFromLocation(self, LocationID):
		try: 	result = self.cl.service.GetWarehouseFromLocation(LocationID)
		except:	result = "Error"
		return result

	def ListAllBins(self, LocationID):
		try: 	result = self.cl.service.ListAllBins(LocationID)
		except:	result = "Error"
		return result

	def ProductKit_ListKitItems(self, MainProductID):
		try: 	result = self.cl.service.ProductKit_ListKitItems(MainProductID)
		except:	result = "Error"
		return result

	def Manufacturer_GetManufacturer(self, ManufacturerID):
		try: 	result = self.cl.service.Manufacturer_GetManufacturer(ManufacturerID)
		except:	result = "Error"
		return result

	def GetProductUPC(self, MasterSKU):
		try: 	result = self.cl.service.GetProductUPC(MasterSKU)
		except:	result = "Error"
		return result

	def RatesSettings_Get(self, merchantID):
		try: 	result = self.cl.service.RatesSettings_Get(merchantID)
		except:	result = "Error"
		return result

	def Orders_Confirm(self, oID):
		try: 	result = self.cl.service.Orders_Confirm(oID)
		except:	result = "Error"
		return result

	def Orders_Unship(self, oID):
		try: 	result = self.cl.service.Orders_Unship(oID)
		except:	result = "Error"
		return result

	def Serials_DeleteFor(self, oID):
		try: 	result = self.cl.service.Serials_DeleteFor(oID)
		except:	result = "Error"
		return result

	def Serials_ListFor(self, oID):
		try: 	result = self.cl.service.Serials_ListFor(oID)
		except:	result = "Error"
		return result

	def Orders_ShouldAllowShippingOfOrder(self, OrderCompanyID):
		try: 	result = self.cl.service.Orders_ShouldAllowShippingOfOrder(OrderCompanyID)
		except:	result = "Error"
		return result

	def Orders_ShouldAllowShippingOfUnpaidOrders(self, OrderCompanyID):
		try: 	result = self.cl.service.Orders_ShouldAllowShippingOfUnpaidOrders(OrderCompanyID)
		except:	result = "Error"
		return result

	def Orders_DeletePackage(self, packageID):
		try: 	result = self.cl.service.Orders_DeletePackage(packageID)
		except:	result = "Error"
		return result

	def GetProductOwners(self, pattern):
		try: 	result = self.cl.service.GetProductOwners(pattern)
		except:	result = "Error"
		return result

	def IsImageUsed(self, pattern):
		try: 	result = self.cl.service.IsImageUsed(pattern)
		except:	result = "Error"
		return result

	def PickList_GeneratePickList(self, PickListID):
		try: 	result = self.cl.service.PickList_GeneratePickList(PickListID)
		except:	result = "Error"
		return result

	def PickList_GetDetailedInfo(self, PickListID):
		try: 	result = self.cl.service.PickList_GetDetailedInfo(PickListID)
		except:	result = "Error"
		return result

	def PickList_GetDetails(self, PickListID):
		try: 	result = self.cl.service.PickList_GetDetails(PickListID)
		except:	result = "Error"
		return result

	def PickList_ListOrderIDs(self, PickListID):
		try: 	result = self.cl.service.PickList_ListOrderIDs(PickListID)
		except:	result = "Error"
		return result

	def PickList_Product_ListAll(self, PickListID):
		try: 	result = self.cl.service.PickList_Product_ListAll(PickListID)
		except:	result = "Error"
		return result

	def PickList_ProductOrder_ListClosed(self, PickListID):
		try: 	result = self.cl.service.PickList_ProductOrder_ListClosed(PickListID)
		except:	result = "Error"
		return result

	def PickList_ProductOrder_ListOpen(self, PickListID):
		try: 	result = self.cl.service.PickList_ProductOrder_ListOpen(PickListID)
		except:	result = "Error"
		return result

	def OrderPackages_Delete(self, pID):
		try: 	result = self.cl.service.OrderPackages_Delete(pID)
		except:	result = "Error"
		return result

	def OrderPackages_GetPackageByID(self, pID):
		try: 	result = self.cl.service.OrderPackages_GetPackageByID(pID)
		except:	result = "Error"
		return result

	def Orders_GetBundleDefinitions(self, pID):
		try: 	result = self.cl.service.Orders_GetBundleDefinitions(pID)
		except:	result = "Error"
		return result

	def POItem_GetAllOfOrder(self, POID):
		try: 	result = self.cl.service.POItem_GetAllOfOrder(POID)
		except:	result = "Error"
		return result

	def PurchaseOrderItem_GetAllOfOrder(self, POID):
		try: 	result = self.cl.service.PurchaseOrderItem_GetAllOfOrder(POID)
		except:	result = "Error"
		return result

	def POItem_Get(self, POID):
		try: 	result = self.cl.service.POItem_Get(POID)
		except:	result = "Error"
		return result

	def ProductIdentifier_GetSku(self, ProductIdentifier):
		try: 	result = self.cl.service.ProductIdentifier_GetSku(ProductIdentifier)
		except:	result = "Error"
		return result

	def ProductIdentifier_WithReplacements_GetSku(self, ProductIdentifier):
		try: 	result = self.cl.service.ProductIdentifier_WithReplacements_GetSku(ProductIdentifier)
		except:	result = "Error"
		return result

	def GetAbbreviatedProductInfo(self, ProductIDorUPC):
		try: 	result = self.cl.service.GetAbbreviatedProductInfo(ProductIDorUPC)
		except:	result = "Error"
		return result

	def KitParent_Find(self, ProductIDorUPC):
		try: 	result = self.cl.service.KitParent_Find(ProductIDorUPC)
		except:	result = "Error"
		return result

	def KitParent_FindRelated(self, ProductIDorUPC):
		try: 	result = self.cl.service.KitParent_FindRelated(ProductIDorUPC)
		except:	result = "Error"
		return result

	def PickList_Product_GetOrder(self, ProductIDorUPC):
		try: 	result = self.cl.service.PickList_Product_GetOrder(ProductIDorUPC)
		except:	result = "Error"
		return result

	def Product_FindMatchingProducts(self, ProductIDorUPC):
		try: 	result = self.cl.service.Product_FindMatchingProducts(ProductIDorUPC)
		except:	result = "Error"
		return result

	def GetPurchaseOrderByID(self, PurchaseOrderId):
		try: 	result = self.cl.service.GetPurchaseOrderByID(PurchaseOrderId)
		except:	result = "Error"
		return result

	def ProductLocation_RemoveQuantitiesOfAPurchaseOrder(self, PurchaseOrderId):
		try: 	result = self.cl.service.ProductLocation_RemoveQuantitiesOfAPurchaseOrder(PurchaseOrderId)
		except:	result = "Error"
		return result

	def UpdatePurchaseOrderAsExported(self, PurchaseOrderId):
		try: 	result = self.cl.service.UpdatePurchaseOrderAsExported(PurchaseOrderId)
		except:	result = "Error"
		return result

	def ProductRebate_Delete(self, RebateID):
		try: 	result = self.cl.service.ProductRebate_Delete(RebateID)
		except:	result = "Error"
		return result

	def ProductRebate_GetByID(self, RebateID):
		try: 	result = self.cl.service.ProductRebate_GetByID(RebateID)
		except:	result = "Error"
		return result

	def UpdateRefundAsExported(self, ReturnID):
		try: 	result = self.cl.service.UpdateRefundAsExported(ReturnID)
		except:	result = "Error"
		return result

	def UpdateReturnAsExported(self, ReturnID):
		try: 	result = self.cl.service.UpdateReturnAsExported(ReturnID)
		except:	result = "Error"
		return result

	def GetClientSetting(self, SettingName):
		try: 	result = self.cl.service.GetClientSetting(SettingName)
		except:	result = "Error"
		return result

	def GetProductParent(self, ShadowSKU):
		try: 	result = self.cl.service.GetProductParent(ShadowSKU)
		except:	result = "Error"
		return result

	def Products_GetInformation(self, SKU):
		try: 	result = self.cl.service.Products_GetInformation(SKU)
		except:	result = "Error"
		return result

	def Orders_GetDataSourceOrderID(self, sourceOrderId):
		try: 	result = self.cl.service.Orders_GetDataSourceOrderID(sourceOrderId)
		except:	result = "Error"
		return result

	def GetWarehouseFromStation(self, StationID):
		try: 	result = self.cl.service.GetWarehouseFromStation(StationID)
		except:	result = "Error"
		return result

	def Orders_GetOrderIdFromTrackingNumber(self, TrackingNumber):
		try: 	result = self.cl.service.Orders_GetOrderIdFromTrackingNumber(TrackingNumber)
		except:	result = "Error"
		return result

	def Orders_GetShippedVerified(self, TrackingNumber):
		try: 	result = self.cl.service.Orders_GetShippedVerified(TrackingNumber)
		except:	result = "Error"
		return result

	def Orders_UpdateShippedVerified(self, TrackingNumber):
		try: 	result = self.cl.service.Orders_UpdateShippedVerified(TrackingNumber)
		except:	result = "Error"
		return result

	def Orders_UpdateShippedVerifiedUndo(self, TrackingNumber):
		try: 	result = self.cl.service.Orders_UpdateShippedVerifiedUndo(TrackingNumber)
		except:	result = "Error"
		return result

	def WarehouseInventoryTransferRequest_Delete(self, TransferRequestID):
		try: 	result = self.cl.service.WarehouseInventoryTransferRequest_Delete(TransferRequestID)
		except:	result = "Error"
		return result
