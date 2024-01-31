from xknx import XKNX
from xknx.devices import Light
from xknx.io import ConnectionConfig, ConnectionType
from xknx.tools import group_value_write

# Eventuell bastle ich hoer bereits Filtertabellen ein, sodass entsprechende Telegramme tatsächglich nur an den jewieligen IP-Koppler geschickt werden.
# Aktuell ist eine filtertabelle aber aus der ETS in den Linienkopplern hinterlegt, daher ist's eigentlich egal. -> Weite Zukunft

connection_config_altbau = ConnectionConfig(
    connection_type=ConnectionType.TUNNELING,
    gateway_ip="X.X.X.X")

connection_config_neubau = ConnectionConfig(
    connection_type=ConnectionType.TUNNELING,
    gateway_ip="X.X.X.X")

connection_config_turnhalle = ConnectionConfig(
    connection_type=ConnectionType.TUNNELING,
    gateway_ip="X.X.X.X")


async def write(group_address: str, value: int):
    print(f"\033[96m\033[1mWriting {value} to {group_address} \033[0;0m")
    async with XKNX(connection_config=connection_config_altbau) as knx_altbau:
        await group_value_write(knx_altbau, group_address, value)
    async with XKNX(connection_config=connection_config_neubau) as knx_neubau:
        await group_value_write(knx_neubau, group_address, value)
    async with XKNX(connection_config=connection_config_turnhalle) as knx_turnhalle:
        await group_value_write(knx_turnhalle, group_address, value)


async def switch_light(name: str, group_address_switch: str, value: int):
    print(f"\033[96m\033[1mSwitching {name} ({group_address_switch}) to {'on' if value else 'off'} \033[0;0m")
    async with XKNX(connection_config=connection_config_altbau) as knx_altbau:
        light_altbau = Light(knx_altbau, name=name, group_address_switch=group_address_switch)
        if value == 0:
            await light_altbau.set_off()
        elif value == 1:
            await light_altbau.set_on()
        else:
            raise ValueError("Value must be 0 or 1")
    async with XKNX(connection_config=connection_config_neubau) as knx_neubau:
        light_neubau = Light(knx_neubau, name=name, group_address_switch=group_address_switch)
        if value == 0:
            await light_neubau.set_off()
        elif value == 1:
            await light_neubau.set_on()
        else:
            raise ValueError("Value must be 0 or 1")
    async with XKNX(connection_config=connection_config_turnhalle) as knx_turnhalle:
        light_turnhalle = Light(knx_turnhalle, name=name, group_address_switch=group_address_switch)
        if value == 0:
            await light_turnhalle.set_off()
        elif value == 1:
            await light_turnhalle.set_on()
        else:
            raise ValueError("Value must be 0 or 1")


async def dimm_light(name: str, group_address_dimm: str, value: int):
    print(f"\033[96m\033[1mDimming {name} ({group_address_dimm}) to {value}% \033[0;0m")
    async with XKNX(connection_config=connection_config_altbau) as knx_altbau:
        light_altbau = Light(knx_altbau, name=name, group_address_brightness=group_address_dimm)
        await light_altbau.set_brightness(value)
    async with XKNX(connection_config=connection_config_neubau) as knx_neubau:
        light_neubau = Light(knx_neubau, name=name, group_address_brightness=group_address_dimm)
        await light_neubau.set_brightness(value)
    async with XKNX(connection_config=connection_config_turnhalle) as knx_turnhalle:
        light_turnhalle = Light(knx_turnhalle, name=name, group_address_brightness=group_address_dimm)
        await light_turnhalle.set_brightness(value)
