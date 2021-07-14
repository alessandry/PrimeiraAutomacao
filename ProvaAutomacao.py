#IMPORTANDO O WEBDRIVER DO CHROME
import self as self
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
import time
import select

#VINCULANDO O NAVEGADOR A VARIAVEL
driver = webdriver.Chrome()

#ABRINDO O SITE E ADICIONANDO UM ITEM AO CARRINHO
driver.get("http://www.automationpractice.com")
driver.find_element_by_xpath('//*[@id="homefeatured"]/li[2]/div/div[2]/h5/a').click()
driver.find_element_by_xpath('//*[@id="add_to_cart"]/button/span').click()
#sleep aguardando a layer abrir
time.sleep(5)
driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span').click()
time.sleep(5)

#TESTA SE O PRODUTO COLOCADO NO CARRINHO É O INDICADO NO CODIGO
try:
    driver.get("http://automationpractice.com/index.php?controller=order")
    elemento = driver.find_element_by_xpath('//*[@id="product_2_7_0_0"]/td[2]/p/a').text
    assert elemento == 'Blouse'
    print("Produto Encontrado")
    #CASO SEJA ENCONTRADO, ENCAMINHA PARA O CHECKOUT
    driver.find_element_by_xpath('//*[@id="center_column"]/p[2]/a[1]/span').click()
except AssertionError:
    print("Produto nao encontrado")
    # CASO NAO SEJA O ITEM VOLTA PARA A TELA INICIAL
    driver.find_element_by_xpath('//*[@id="header_logo"]/a/img').click()

time.sleep(2)
username = driver.find_element_by_id('email_create')
username.send_keys('testedbserver26@dbserver.com.br')
driver.find_element_by_xpath('//*[@id="SubmitCreate"]/span').click()
time.sleep(3)
driver.find_element_by_id('id_gender1').click()
firstname = driver.find_element_by_id('customer_firstname')
firstname.send_keys('Alessandry')
lastname = driver.find_element_by_id('customer_lastname')
lastname.send_keys('Barbieri')
password = driver.find_element_by_id('passwd')
password.send_keys('12345')
endereco = driver.find_element_by_id('address1')
endereco.send_keys('5th Avenue')
cidade = driver.find_element_by_id('city')
cidade.send_keys('New York')
select = Select(driver.find_element_by_id('id_state'))
select.select_by_value('32')
cep = driver.find_element_by_id('postcode')
cep.send_keys('10001')
country = driver.find_element_by_id('uniform-id_country')
country.click()
telefone = driver.find_element_by_id('phone_mobile')
telefone.send_keys('51982730769')
driver.find_element_by_xpath('//*[@id="submitAccount"]/span').click()
time.sleep(3)

try:
    driver.get('http://automationpractice.com/index.php?controller=order&step=1&multi-shipping=0')
    verificaEndereco = driver.find_element_by_xpath('//*[@id="address_delivery"]/li[3]').text
    assert verificaEndereco == '5th Avenue'
    print("Endereco Validado")
    #CASO SEJA ENCONTRADO, ENCAMINHA PARA O CHECKOUT
    driver.find_element_by_xpath('//*[@id="center_column"]/form/p/button/span').click()


except AssertionError:
    print("Endereco Incorreto")
    # CASO NAO SEJA O ITEM VOLTA PARA A TELA INICIAL
    driver.find_element_by_xpath('//*[@id="header_logo"]/a/img').click()

time.sleep(2)
driver.find_element_by_id('cgv').click()
driver.find_element_by_xpath('//*[@id="form"]/p/button/span').click()


try:
    driver.get('http://automationpractice.com/index.php?controller=order&multi-shipping=')
    verificaValor = driver.find_element_by_xpath('//*[@id="total_price"]').text
    assert verificaValor == '$29.00'
    print("Valor Validado")
    #CASO SEJA ENCONTRADO, ENCAMINHA PARA O CHECKOUT
    driver.find_element_by_xpath('//*[@id="center_column"]/p[2]/a[1]/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="center_column"]/form/p/button/span').click()
    time.sleep(2)
    #driver.find_element_by_xpath('//*[@id="form"]/p/button/span').click()
    #time.sleep(2)
    driver.find_element_by_id('cgv').click()
    driver.find_element_by_xpath('//*[@id="form"]/p/button/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a').click()
    driver.find_element_by_xpath('//*[@id="cart_navigation"]/button/span').click()

except AssertionError:
    print("Valor Incorreto")
    driver.find_element_by_xpath('//*[@id="cart_navigation"]/button/span').click()



