import asyncio
import yaml

from gateway_communicator import write, switch_light, dimm_light

with open('./Backend/lights_config.yaml', 'r') as file:
    config_data_light = yaml.safe_load(file)

with open('./Backend/jalousien_config.yaml', 'r') as file:
    config_data_jalousie = yaml.safe_load(file)


async def licht_schalten(group: str, value: int):
    for light in config_data_light.get(group, []):
        await switch_light(light['name'], light['group_address_switch'], value)


async def licht_dimmen(group: str, value: int):
    for light in config_data_light.get(group, []):
        await dimm_light(light['name'], light['group_address_brightness'], value)


async def jalousie_fahren(group: str, value: int):
    for jalousie in config_data_jalousie.get(group, []):
        await dimm_light(jalousie['name'], jalousie['group_address_switch'], value)

# nice, dimm_light geht auch für unsere Jalousienakoren, hehe
