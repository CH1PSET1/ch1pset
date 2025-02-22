import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.components import uart, sensor
from esphome.const import CONF_ID, CONF_UART_ID

# Создаем пространство имен для компонента
mercury_ns = cg.esphome_ns.namespace("mercury")
Mercury = mercury_ns.class_("Mercury", cg.polling_component.PollingComponent, uart.UARTDevice)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(Mercury),
    cv.Required(CONF_UART_ID): cv.use_id(uart.UARTComponent),
}).extend(cv.polling_component.POLLING_COMPONENT_SCHEMA).extend(cv.COMPONENT_SCHEMA.schema)

def to_code(config):
    uart_var = cg.get_variable(config[CONF_UART_ID])
    # Получаем указатели на датчики – имена (id) должны совпадать с теми, что вы используете в YAML
    volts = yield cg.get_variable("Volts")
    amps = yield cg.get_variable("Amps")
    watts = yield cg.get_variable("Watts")
    tariff1 = yield cg.get_variable("Tariff1")
    tariff2 = yield cg.get_variable("Tariff2")
    sum_tariff = yield cg.get_variable("Sum_Tariff")
    cg.new_Pvariable(config[CONF_ID], uart_var, volts, amps, watts, tariff1, tariff2, sum_tariff)
