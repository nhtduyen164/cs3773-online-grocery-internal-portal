[InternalGrocerySystemClassDiagram.class.violet.html](https://github.com/user-attachments/files/29420130/InternalGrocerySystemClassDiagram.class.violet.html)

<HTML>
<HEAD>
<META name="description"
	content="Violet UML Editor cross format document" />
<META name="keywords" content="Violet, UML" />
<META charset="UTF-8" />
<SCRIPT type="text/javascript">
	function switchVisibility() {
		var obj = document.getElementById("content");
		obj.style.display = (obj.style.display == "block") ? "none" : "block";
	}
</SCRIPT>
</HEAD>
<BODY>
	This file was generated with Violet UML Editor 3.0.0.
	&nbsp;&nbsp;(&nbsp;<A href=# onclick="switchVisibility()">View Source</A>&nbsp;/&nbsp;<A href="http://sourceforge.net/projects/violet/files/violetumleditor/" target="_blank">Download Violet</A>&nbsp;)
	<BR />
	<BR />
	<SCRIPT id="content" type="text/xml"><![CDATA[<ClassDiagramGraph id="1">
  <nodes id="2">
    <ClassNode id="3">
      <children id="4"/>
      <location class="Point" id="5">490.0,170.0</location>
      <id id="6" value="4789ca4f-f90f-4f5e-abbd-e5a658d5f5ec"/>
      <revision>1</revision>
      <backgroundColor id="7">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
        <alpha>255</alpha>
      </backgroundColor>
      <borderColor id="8">
        <red>191</red>
        <green>191</green>
        <blue>191</blue>
        <alpha>255</alpha>
      </borderColor>
      <textColor id="9">
        <red>51</red>
        <green>51</green>
        <blue>51</blue>
        <alpha>255</alpha>
      </textColor>
      <preferredSize class="Rectangle" id="10">0.0,0.0,0.0,0.0</preferredSize>
      <name id="11" justification="1" size="3" underlined="false">
        <text>Product</text>
      </name>
      <attributes id="12" justification="0" size="4" underlined="false">
        <text>+prod_id : int
+prod_name : str
+prod_count : int</text>
      </attributes>
      <methods id="13" justification="0" size="4" underlined="false">
        <text>+__init__(prod_id: int, prod_name: str, prod_count: int)
+get_prod_id() : int
+get_prod_name() : str
+get_prod_count() : int
+set_prod_id(prod_id: int) : None
+set_prod_name(prod_name: str) : None
+set_prod_count(prod_count: int) : None</text>
      </methods>
    </ClassNode>
    <ClassNode id="14">
      <children id="15"/>
      <location class="Point" id="16">540.0,520.0</location>
      <id id="17" value="d9f7137e-11e9-4814-ad10-1cd3fdd6d7b9"/>
      <revision>1</revision>
      <backgroundColor reference="7"/>
      <borderColor reference="8"/>
      <textColor reference="9"/>
      <preferredSize class="Rectangle" reference="10"/>
      <name id="18" justification="1" size="3" underlined="false">
        <text>ProductManager</text>
      </name>
      <attributes id="19" justification="0" size="4" underlined="false">
        <text>+products : list[Product]</text>
      </attributes>
      <methods id="20" justification="0" size="4" underlined="false">
        <text>+__init__()
+add_product(product: Product) : None
+load_products() : None
+find_product(prod_id: int) : Product
+remove_product(product: Product) : None
+update_product(product: Product): None</text>
      </methods>
    </ClassNode>
  </nodes>
  <edges id="21">
    <AggregationEdge id="22">
      <start class="ClassNode" reference="3"/>
      <end class="ClassNode" reference="14"/>
      <startLocation class="Point" id="23">150.0,250.0</startLocation>
      <endLocation class="Point" id="24">100.0,40.0</endLocation>
      <id id="25" value="af816e5c-eba9-4cf9-827c-12e14614825f"/>
      <revision>1</revision>
      <bentStyle name="AUTO"/>
      <startLabel></startLabel>
      <middleLabel></middleLabel>
      <endLabel></endLabel>
    </AggregationEdge>
  </edges>
</ClassDiagramGraph>]]></SCRIPT>
	<BR />
	<BR />
	<IMG alt="embedded diagram image" src="data:image/png;base64,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
KQBLmHigwxSAJUw80GEKwBImHugwBWAJEw90mAKwhIkHOkwBWMLEAx2mACxh4oEOUwCWMPFAhykA
S5h4oMMUgCVMPNBhCsASJh7oMAVgCRMPdJgCsISJBzpMAVjCxAMdpgAsYeKBDlMAljDxQIcpAEuY
eKDDFIAlTDzQYQrAEiYe6DAFYAkTD3SYArCEiQc6TAFYwsQDHaYALGHigQ5TAJYw8UCHKQBLmHig
wxSAJUw80GEKwBImHugwBWAJEw90mAKwhIkHOkwBWMLE89j48A8HXIBlKGqgw5iAZShqoMOYgGUo
aqDDmIBlKGqgw5iAZShqoMOYgGUoaqDDmIBlKGqgw5iAZShqoMOYgGUoaqDDmIBlKGqgw5iAZShq
oMOYgGUoaqDDmIBlKGqgw5iAZShqoMOYgGUoaqDDmIBlKGqgw5iAZShqoMOYgGUoaqDDmIBlKGqg
w5iAZShqoMOYgGUoaqDDmIBlKGqgw5iAZShqoMOYgGUoaqDDmIBlKGqgw5iAZShqoMOYgGUoXr75
5puf/exn9NdfASIHOixeFi5c+Itf/IL++itA5ECHRcrFixd/+ctf/vOf/6S/VPZXg2iBDouU6urq
P/7xj1Sgv1T2V4NogQ6LkVOnTv36179++PAhlekvlSnibwQiBDosOlThybIEToAOiw7tjSjfpgIn
QIfFxd27d7VfzIivbajWFwfRAB0WF2+++eZYP1RQnGr9URAJ0GFx8atf/er8+fP+aBaKU60/CiIB
OiwucD2MJ9BhcYHnw3gCHRYd+L40hkCHRQd+P4wh0GExgn9PEzegwyIF/740VkCHRYr4YubLL7/U
fm0DIgY6LF4WLlz485//fKyfMUCUxFSH/wfs09TU9Nhjj9FffwWwgD/FRxNfHfpDwAL/+Mc//CFg
AWM+Q4cAWMeYz9AhANYx5jN0CIB1jPkMHQJgHWM+Q4cAWMeYz9AhANYx5jN0CIB1jPkMHQJgHWM+
Q4cAWMeYz9AhANYx5jN0CIB1jPkMHQJgHWM+Q4cAWMeYz9AhANYx5jN0GDXeCE888cSkSZMaGxvv
3LnjbxQCMYg/GkhnZ+fLL78syjyNW7du0ce///3vHBnVBxQCYz5Dh1HDuT4wMLBnzx4qv/HGG/5G
IchDM3IXUSb+8pe/0McDBw5wZFQfUAiM+QwdRo2c6319fVSurKzk+KpVqxYvXpzJ/m/U3nnnnaqq
qqeffvr9998fHh6mYHd397Jly5555pljx47xOPKAXB4aGnr33XenTp1aUVGxYsWK7777TlRxA1GY
OXPm1q1b6eO6detmzZrFtd9++y31ost1WVnZvHnzvvrqK+7yxRdfvPDCCzSHv/71r2O17O3tpR2h
NkeOHOExaY92795dU1NDs/rd734n/m9xopb3Oq0Y8xk6jBrOS+KHH36gMiUxx1tbWymJ6ePevXvp
4yeffPLxxx9T4eDBgxTcvHkzlZubm7dv387jyANy+cMPP6TC0aNHz58/T4WGhgZtyw0bNtTV1dHH
2trajRs3coMXX3zxz3/+83//+98rV65QhBTFXX7729/+7W9/owLpdqyWb731lped55tvvsljfvTR
RyJ48uRJKtDJhcfkvU4rxnyGDqOG8/LBgwd0xaOyeKuEiPP/2X7GjBn0kS6At2/fpoJQC11JqEzP
kxTncbggl2fPni1airivlsvHjx+nv+Lh8MSJE3KDy5cv0/Tmzp3rZR9luQsJZnBwkIPaltOmTRMt
b968yWM+++yzInj//n0veynmMVP///M35jN0GDUi87xsytJt56ZNm0QWiqC4/yRKS0vp48MsVJg4
cSIF6d5PtCFEe+5IhUePHnGZW/J25ZZc/te//kV/16xZQ3///e9/cwO6DnvZ20X+/kbbfayWYvK0
dbo95qCYEjNhwgQexzfP9GHMZ+gwakTm+aNK3Hc9nDNnTka6zogbWtGe9OxlFdvT08NBcT2kCA+Y
GUNIkydPfvzxx+mvHKSnSircy8JBLhhbius2bf3WrVscnD59umgpRvCNk26M+QwdRs1YmeeLv/fe
e570fEiFzMhz15EjR3bt2sXtheToOfDtt9/moPgmllpeuHCBCvQUR8Enn3zSG7kJ5JaNjY1UeO21
1+Sg0AyN+ac//YmDXDC25OdDutpzkPeos7OTCuIXFK5NN8Z8hg6jZqzM88XpGYzEJr4v/eCDD+ie
M5P9HnLZsmVPPfWU/D0kaaCmpua55567ePEiB6k7PbPV1tbS9WrlypU3btyg4GeffVZeXk73kPLm
Dh486I18D8TBM2fO0JhTpkwxfiGkbUmX8UWLFtFVUcxT3FQPDAxQG9ojmsOrr776/fff+8ZMMcZ8
hg5B4amurt63b9/9+/evXr1KMqNzh79FkWHMZ+gQFJ729vb58+fTda+srGzp0qVdXV3+FkWGMZ+h
QwCsY8xn6BAA6xjzGToEwDrGfIYOAbCOMZ+hQwCsY8xn6BAA6xjzGToEwDrGfIYOAbCOMZ+hQwCs
Y8xn6BAA6xjzGToEwDrGfIYOAbCOMZ+hQwCsY8zn+OoQgDThT/HRxFeH/hAAicWYz9AhANYx5jN0
CIB1jPkMHQJgHWM+Q4cAWMeYz9AhANYx5jN0CIB1jPkMHQJgHWM+Q4cAWMeYz9AhANYx5jN0CIB1
jPkMHQJgHWM+Q4cAWMeYz9AhANYx5jN0GIqhoSF/qKDYHj8kMZlG+jDmc5HqMNd37onX8eaB/MLA
0TWj4PH5fYCiQJSUlDQ0NFy7dm1Uh3AEb1RFTIPnAAqFMZ+hw1Dk2p4J2ZGbqQW6RjU3N7/00kvi
Y06E3Dqjbh0UBGM+J0OHvrSgj62trZWVlYsXL759+zYH9+7dO3/+fCrfuXNn9erVkyZNWrNmDZVF
g56enqVLl1LwxIkT2oTjcldXV319/eTJk8+dOyfigkz29bd0gSorK1u4cOGFCxe4r0BNX3VD6gjy
+Gp7or+/v6KiguMR7KbcHoyf1Opww4YNfX19hw4d2rx5MwePHj0qXv6+Y8eOw4cP379/nxps375d
NNiyZcuRI0fu3btHheAEXbdu3f79+zs6OmbNmuWrIgnRVoaHh0+fPj179mwRDEDdkHYEtRkXHjx4
QJOhMw7HI9hNuT0YP4nXoTcaDl6/fj2TvSBMmTKFg3xtnDFjhrg+0N+pU6eKYG1trUjfGzduyEOJ
glyurq7u7u7muFy1fPlySt/z58/TNUpuMBbqhrQjqM1G9tijK6f8fBjNbsrtwfhJvA4FvrSgj4OD
g1R4+PAhXV44+OjRI1Gm3KULDhXoLzeYMGGCCFJfbcJxmVuqVZS4S5YsKS0tLS8vv3LlitxGi7oh
7Qhqs7GUEM1ujrV1kB+p1eGtW7eo0NvbO23aNLUNXRzobk00qKmp4SB9pMLNmzfVhKPHKi5TF9GS
8U1gYGDg+PHjfCkOQN2QwDeC2mwsJUSzm2NtHeRHSnTog7KEHo0oBQ8cOLBz504OcoOtW7e2tLTQ
kxU9OG3cuFEE6Qlq37599OC0bds2bkyXkTNnztAtInXhIN03NjU1dXZ28oMTNRN3g/X19a2trXQd
Fl+3iNoA1MzWjsDjq+19RLObY20d5EdwPmeSq8ODBw9WVFSsXbuWEo6D3IDO+q+88grd+K1cuZLK
ItjX17dq1Sq6BFHucuO2tjZKvqqqqubmZg52dXXNnTuXLhft7e0isn79+okTJ1Lh0qVL8+bNozs6
kdmillHTV9WVdgQeX23vI5rdHGvrID+C8zmTXB36Q2khJrsWk2mkhuB8zkCHccPL4o9GSxzmkDKC
8zmTUB0CkCyM+QwdAmAdYz5DhwBYx5jP0CEA1jHmM3QIgHWM+QwdAmAdYz5DhwBYx5jP0CEA1jHm
M3QIgHWM+QwdAmAdYz5DhwBYx5jP0CEA1jHmM3QIgHWM+RxfHQKQJvwpPpr46tAfAiCxGPMZOgTA
OsZ8hg4BsI4xn6FDAKxjzGfoEADrGPMZOgTAOsZ8hg4BsI4xn6FDAKxjzGfoEADrGPMZOgTAOsZ8
hg4BsI4xn6FDAKxjzGfoEADrGPMZOgTAOsZ8hg7/x9DQkD8EQOEw5nPKdRj83iKunTNnzuiaUJw5
c+b1119ft26d+iJEAGSM+ZxyHYYkWK5aBgYGZs+e/X2WZ599lj76WwAwgjGfk6HDPHQi4I5UOHTo
0IwZM0pKSnhwUSte95frJk6cOLF582ZRpgJ9HF0PwE9Ahz/pcMeOHQ8ePBBvqFZrRSE8K1asOH/+
vChTYeXKlaPrAfiJxOuQL1aCUY1CICvt9u3batBXCM/kyZN7e3tFuaenhz6OrgfgJxKvQ0EeOhFo
laYG8xifLqoPHz4U5aGhIb7GAqACHWqUpgbzGL+mpoYvsFSora0dXQ/AT6REh3mjVZoapKsZiyok
q1atOnfunCh/+eWXr7766uh6AH7CmM/Q4f9Yv379xIkTuUEYjh8/Ln9f2tLSMroegJ8w5nPKdWiP
gYGBGTNm3Moyc+bMwcFBfwsARjDmc/J06IXG39OEv//YiPZffPHFa6+91tjY2NbWNnokAEYRkM+C
5OkQgMRhzGfoEADrGPMZOgTAOsZ8hg4BsI4xn6FDZ8TE9BiTaTBxm09BMOZzOnXIX2kagwUk1/Fl
06OwMkqV+TOeafjg74dLSkoaGhquXbvmbxGC/OYT3tVJ43/66ae+iPwxDhjzGTosGLmOz+3Zyji6
Pk/ynoYKV9E1qrm5+aWXXhpdH4qA8bWI9uFdndR+wYIF8tHLdYsRYMznZOjQd2QvX75Mp+fy8vLa
2tpTp06JYE9Pz9KlSydNmnTixAlurw1qodrW1tbKysrFixfLzoy9e/fOnz+fynfu3Fm9ejUNtWbN
GiqLBtrx5Q1xuaurq76+fvLkyeJfw3kjZEZbGR1OQ24vkCP9/f0VFRUcj2A+WlendpKdnZ3y3QS3
0c7N0zlR7927R1dgOuyNjY33798XwQKSTh3SrUtbWxudLE+ePFldXS2CW7ZsOXLkCB1QKnB7bVAL
1W7YsKGvr48WSVbF0aNH7969S+UdO3YcPnyYFokabN++XTTQji9viMu0zPv37+/o6Jg1a5avSrYy
OpyGClc9ePCAetGpgeMRzCekq1O037p1K9/H8gjauXk6J+quXbuuXr1KGfX555/v3r1bBAtI4nXo
jWZUo+z9Egfp2igy48aNG8FBLVR7/fr1TPYkOmXKFA7yRYnOoOKcSn+nTp0qgtrx5Q1xmc4X3d3d
HJerZCujw2moeCOUlZXJz4fRzCekq1O0pzPXCy+8QH85khljbvLkueX06dOFi214eHjmzJkiWEAS
r0OBvIQEZS3dF9GplA40V02YMIEOIhUGBweDg1qoVvwbUVoP2bD/6NEjUaZcFEPRX26gHV+bcNxS
rZKtjA6noTJWVTTzCenq5PZ0faOrohzRzk07DWrpjVBaWsoNCkU6dbho0aI9e/a0t7fTvQRX0QlP
XFVu3rwZHNRCtbdu3cpkRT5t2jQOcgMaSjw5UIOamhoOquNzgc7oXKYufNETyFXyGdrVNFTGqopm
PiFdnfJk6NRMz4oc0c5Nbi+3tPp7SUp06IOep69cuUJ3PvQExYeSHgD27dtHzyTbtm0LDmrxso8N
tGwHDhzYuXMnB7kBnWtbWlrouYIeNjZu3CiC2vHp1EvPKv39/dSFg5QiTU1NlCX8IMSmR9nK6HAa
KmMdsWjmE9LVKU/m+++/X7BgAUe0c5Pbyy2//vprej48duwY3YFzg0IRnM+ZhOqQ7kDq6uroHEbH
lw8lPRtQQtMzFR364KAWqj148GBFRcXatWspgTjIDegs/sorr5SXl69cuZLKIqgdX3wBUFVV1dzc
zMGurq65c+fSWZku4yLCpkfZyuhwGurxUSOCaOajdXWqU/JFSEgc0c5Nbs9leoCkA06H/fnnn8/v
Z9JggvM5k1Ad2kBd4MhgK2PG6TRiRcpcncZ8LjodejpE3N80QoSVMeN6GvEhZa5OYz4XnQ4BiB5j
PkOHAFjHmM/QIQDWMeYzdAiAdYz5DB26x+ovyCAOGPM5kToc55eK4+xuJNfxAxyAglxftOglwZJX
VATncwY6tEGu4we3z+NFi14SLHlFRXA+Z5KiQ18a8UetwSy8O1GL584BSJe7kpKSsrKyhQsXXrhw
QbQ3vmhR3R0vCZa8oiLlOtQazMK7E7V47hyAJAPayvDw8OnTp+kaKIJ5vGhRDBhzS15RkXgdeqPh
oChoDWaM0Z2oxXPnAFy+fDmplMTW39/PtXm8aFEMGHNLXlGReB0KfMrhj1qDWXh3ohbPnQOQ9Llk
yZLS0lK6qb5y5YoIluT+okUeMM6WvKIi5TrUGszCuxO1eK4dgHQrePz4cb4U5/GiRXnA2FryioqU
6NAH54rWYBbenajFc+cArK+vb21tpauf+MJG1ObxokV5trG15BUVwfmcSboOtQaz8O5ELZ47B+Cl
S5fmzZtHN65CwKLW+KJFdXd8kXha8oqK4HzOJFSHVlHT2i140WIKMOZz8erQ0yHi/qauwYsWk44x
n4tXhwBEhjGfoUMArGPMZ+gQAOsY8xk6BMA6xnyGDt2Qgp/IE7ELMZmkMZ8TqcMzZ86Ulpbu3r07
/Heb4VvmR67jO3n5obZWGxQEVGXyelGhoCTytyk6JzifMwnVofiZ2/evNIPJdf1yJdfxub3blx9m
8uoiEB1zckWKQvRvU3ROcD5nkqJD+Wj+eFLNRjju6Rx0Wk+gFs+d59DSyw+1cK22i9pXrvIdXnkX
wrsiuRz92xTdkkIdyh/lguqg03oCtXjuPIeWXn6ohWtDdgk+vFybkysy4+htim5JvA690XBQLagO
Oq0nUIvnznNo6eWHWnI9MsGHlwvhXZECJ29TdEvidSjwHU11MbSrovUEavHceQ5le2EBp6FFnU9w
l+Cd4kKurkgf+e2gdkoBx9ktRa1DrSdQi+fOcyjbCws4DS25Hhl1p7TBPFyRMvntYK7H2S0p0aEP
dTG0iaL1BGrx3HkOLb38UEuuRyb48PIu5OGKlMlvB3M9zm4JzudMunWo9QRq8dx5Di29/FBL8JFR
+2qruDzOFxUy+e1grsfZLcH5nEmoDgvOWCkSAUl/+SFckWEw5nNx6dDTIeL+phFS8Jcf+vcwi79R
gYArMgzGfC4uHQLgBGM+Q4cAWMeYz9AhANYx5jN0CIB1jPkMHSaSmNjqYjINJm7zYYz5DB3Ggly/
z3RiX1QJcPfx97QlkbsNc7JERvOiSGM+Q4exINfl5/Zu7YsB7bkqerdhTpbIaF4UacznZOjQd3Q8
ybF2T/eaPmrQ0tJSneXs2bMdHR21tbUlkjVR9blRNn/zzTdU+Pbbb+vq6sYaWYtXON+gvKdcDrDV
WbIv5joNub1AjkTvNgxviYzmRZGp1SE71rSv6aMGmzZtooNy+vRpWvI9e/ZQWfbOqT43GofGpAKd
vMU42pG1eIXzDcp7yuUAW50l+2Ku01DhKiduw5wskRG8KDLxOvRGw0E+32tf08cNqIrK8vlMFFSf
21dffUXns0x2dS9evJgZY2QtXuF8g1yQywG2Okv2xVynoeKN4MRtGN4SmYnkRZGJ16FAXgbxUXas
/bjg0mv65AZyXy6rPrfBwcGnn36azmr0aCGqtCNr8QrnG9TONsBWV2LHvpjrNFTGqopmPrlaItss
vygytTrk8lTda/q0x0sua31udD38wx/+QDe03EYdWYtXON8gF0La6izZF3OdhspYVdHMJw9LpNUX
RaZEhz7kw6F9TZ/2eMllrc/t+PHj1IAfFbQja/EK5xssydFWZ8m+mOs0VOTtykQznzwskVZfFBmc
z5kU6PCO7jV92uMll7U+t//85z+/+c1v6NCLj9qRtXiF8w3maquzZF/MdRryVgRqRBDNfPKzRNp7
UWRwPmcSqsO4oS5wZCTdvmiDGFoijfkMHeaAp0PE/U0jpOD2xaQTQ0ukMZ+hQwCsY8xn6BAA6xjz
GToEwDrGfIYOAbCOMZ+hwx8x/hQbB2IyyZhMg4nbfFSM+VxEOgz+OjHASmeP4CmpwHaoJaTt0IvK
bahizGfo8EeCay2R60a5PWyHMqK90XboReU2VDHmczJ06Dte8kcuezr3ndbMdvnyZTpVl5eX19bW
njp1SvQVZMLZyQTaLXqR+OtgO9TOR7YdaucWjdtQpbh0qLrvtGY2uo1pa2ujE+fJkyerq6t944Sx
kwm0W/Qi8dfBdqidT7DtUDSLwG2okngdeqPhILeUg6r7TmtmY+jeSR0zjJ1MoN2iF4m/DrZDjstV
PYG2Q9EsArehSuJ1KJDXw/dRXjPVfac1s1EG0z0SnVbp6KtLHsZOJtBu0YvEX1cC26EEVwXbDrmZ
bbehSsp1KLvRPJ37TmtmW7Ro0Z49e9rb2+kGQ+7OXUJ+D67dojxVrYdNOyXtHgX462A7FGUBVwXb
DuU5WHUbqqREhz5KdG40T+e+05rZ6CH7ypUrdBdET1McLBmxroWxkwm0W5QXT+th005Ju0cB/jrY
DrXzCbYdynOw6jZUCc7nTEJ1qHWjeTr33Vhmtrq6Ojqx0UHnIFvX7oSwkwm0W5QXT+thG2tK6h4F
+OtgO9TOR7YdqjPxRey5DVWC8zmTUB1qUY+7baLfIgPboUoMbYeMMZ+hQzOeDhH3N40Q2A59xNB2
yBjzOT06BCC2GPMZOgTAOsZ8hg4BsI4xn6FDAKxjzGfoEADrGPMZOgTAOsZ8hg4BsI4xn6FDAKxj
zGfoEADrGPMZOgTAOsZ8hg4BsI4xn6FDAKxjzGfoEADrGPM5vjoEIE34U3w0/w9NtbL+NjQSFQAA
AABJRU5ErkJg" />
</BODY>
</HTML>
