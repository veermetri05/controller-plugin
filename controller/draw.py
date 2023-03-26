import os 
from xml.etree import ElementTree
from controller.builders import new_guid
import pkgutil

def drawController(root, controllerId):
    data = pkgutil.get_data(__name__, "statics/controller.xml").decode("utf-8").format(controllerId=controllerId)
    controllerLayer = ElementTree.fromstring(data)
    guids = controllerLayer.findall("*//*[@guid='new_guid']")
    for item in guids:
        item.attrib['guid'] = new_guid()
    root.append(controllerLayer)


def drawSliderUI(root, sliderName):
    sliderUI = ElementTree.fromstring(f'''
              <layer type="group" active="true" exclude_from_rendering="false" version="0.3" desc="{sliderName}">
                <param name="z_depth">
                <real value="0.0000000000"/>
                </param>
                <param name="amount">
                <real value="1.0000000000"/>
                </param>
                <param name="blend_method">
                <integer value="0" static="true"/>
                </param>
                <param name="origin">
                <vector>
                    <x>0.0000000000</x>
                    <y>0.0000000000</y>
                </vector>
                </param>
                <param name="transformation">
                <composite type="transformation">
                    <offset>
                    <vector>
                        <x>0.0000000000</x>
                        <y>0.0000000000</y>
                    </vector>
                    </offset>
                    <angle>
                    <angle value="0.000000"/>
                    </angle>
                    <skew_angle>
                    <angle value="0.000000"/>
                    </skew_angle>
                    <scale>
                    <vector>
                        <x>1.0000000000</x>
                        <y>1.0000000000</y>
                    </vector>
                    </scale>
                </composite>
                </param>
                <param name="canvas">
                <canvas>
                    <layer type="group" active="true" exclude_from_rendering="false" version="0.3" desc="Pointer">
                    <param name="z_depth">
                        <real value="0.0000000000"/>
                    </param>
                    <param name="amount">
                        <real value="1.0000000000"/>
                    </param>
                    <param name="blend_method">
                        <integer value="0" static="true"/>
                    </param>
                    <param name="origin">
                        <vector>
                        <x>0.0000000000</x>
                        <y>0.0000000000</y>
                        </vector>
                    </param>
                    <param name="transformation">
                        <composite type="transformation">
                        <offset>
                            <blinecalcvertex type="vector" amount=":{sliderName}">
                            <bline>
                                <bline type="bline_point">
                                <entry>
                                    <composite guid="737B1DBB99C7B6E8B0D40E94E1B20814" type="bline_point">
                                    <point>
                                        <vector>
                                        <x>-1.6666667461</x>
                                        <y>0.3333333433</y>
                                        </vector>
                                    </point>
                                    <width>
                                        <real value="1.0000000000"/>
                                    </width>
                                    <origin>
                                        <real value="0.9143519402"/>
                                    </origin>
                                    <split>
                                        <bool value="false"/>
                                    </split>
                                    <t1>
                                        <radial_composite type="vector">
                                        <radius>
                                            <real value="0.0000000000"/>
                                        </radius>
                                        <theta>
                                            <angle value="-0.000000"/>
                                        </theta>
                                        </radial_composite>
                                    </t1>
                                    <t2>
                                        <radial_composite type="vector">
                                        <radius>
                                            <real value="0.0000000000"/>
                                        </radius>
                                        <theta>
                                            <angle value="-0.000000"/>
                                        </theta>
                                        </radial_composite>
                                    </t2>
                                    <split_radius>
                                        <bool value="true"/>
                                    </split_radius>
                                    <split_angle>
                                        <bool value="false"/>
                                    </split_angle>
                                    </composite>
                                </entry>
                                <entry>
                                    <composite guid="611C8C4EB7DCDFD0BC1BD4180A27F506" type="bline_point">
                                    <point>
                                        <vector>
                                        <x>1.6666667461</x>
                                        <y>0.3333333433</y>
                                        </vector>
                                    </point>
                                    <width>
                                        <real value="1.0000000000"/>
                                    </width>
                                    <origin>
                                        <real value="0.5000000000"/>
                                    </origin>
                                    <split>
                                        <bool value="false"/>
                                    </split>
                                    <t1>
                                        <radial_composite type="vector">
                                        <radius>
                                            <real value="0.0000000000"/>
                                        </radius>
                                        <theta>
                                            <angle value="0.000000"/>
                                        </theta>
                                        </radial_composite>
                                    </t1>
                                    <t2>
                                        <radial_composite type="vector">
                                        <radius>
                                            <real value="0.0000000000"/>
                                        </radius>
                                        <theta>
                                            <angle value="0.000000"/>
                                        </theta>
                                        </radial_composite>
                                    </t2>
                                    <split_radius>
                                        <bool value="true"/>
                                    </split_radius>
                                    <split_angle>
                                        <bool value="false"/>
                                    </split_angle>
                                    </composite>
                                </entry>
                                </bline>
                            </bline>
                            <loop>
                                <bool value="false"/>
                            </loop>
                            <homogeneous>
                                <bool value="false"/>
                            </homogeneous>
                            </blinecalcvertex>
                        </offset>
                        <angle>
                            <angle value="0.000000"/>
                        </angle>
                        <skew_angle>
                            <angle value="0.000000"/>
                        </skew_angle>
                        <scale>
                            <vector>
                            <x>0.7100870013</x>
                            <y>0.7100870013</y>
                            </vector>
                        </scale>
                        </composite>
                    </param>
                    <param name="canvas">
                        <canvas>
                        <layer type="region" active="true" exclude_from_rendering="false" version="0.1" desc="Pointer">
                            <param name="z_depth">
                            <real value="0.0000000000"/>
                            </param>
                            <param name="amount">
                            <real value="1.0000000000"/>
                            </param>
                            <param name="blend_method">
                            <integer value="0"/>
                            </param>
                            <param name="color">
                            <color>
                                <r>1.000000</r>
                                <g>1.000000</g>
                                <b>1.000000</b>
                                <a>1.000000</a>
                            </color>
                            </param>
                            <param name="origin">
                            <vector>
                                <x>0.0000000000</x>
                                <y>0.0000000000</y>
                            </vector>
                            </param>
                            <param name="invert">
                            <bool value="false"/>
                            </param>
                            <param name="antialias">
                            <bool value="true"/>
                            </param>
                            <param name="feather">
                            <real value="0.0000000000"/>
                            </param>
                            <param name="blurtype">
                            <integer value="1"/>
                            </param>
                            <param name="winding_style">
                            <integer value="0"/>
                            </param>
                            <param name="bline">
                            <bline type="bline_point" loop="true">
                                <entry>
                                <composite guid="1E7B60652ED438133579BEBCE4DA83DF" type="bline_point">
                                    <point>
                                    <vector>
                                        <x>-0.4971296787</x>
                                        <y>0.4305267334</y>
                                    </vector>
                                    </point>
                                    <width>
                                    <real value="1.0000000000"/>
                                    </width>
                                    <origin>
                                    <real value="0.5000000000"/>
                                    </origin>
                                    <split>
                                    <bool value="false"/>
                                    </split>
                                    <t1>
                                    <radial_composite type="vector">
                                        <radius>
                                        <real value="0.0000000000"/>
                                        </radius>
                                        <theta>
                                        <angle value="0.000000"/>
                                        </theta>
                                    </radial_composite>
                                    </t1>
                                    <t2>
                                    <radial_composite type="vector">
                                        <radius>
                                        <real value="0.0000000000"/>
                                        </radius>
                                        <theta>
                                        <angle value="0.000000"/>
                                        </theta>
                                    </radial_composite>
                                    </t2>
                                    <split_radius>
                                    <bool value="true"/>
                                    </split_radius>
                                    <split_angle>
                                    <bool value="false"/>
                                    </split_angle>
                                </composite>
                                </entry>
                                <entry>
                                <composite guid="F834BD4289D00B12E233D07DD05D32E5" type="bline_point">
                                    <point>
                                    <vector>
                                        <x>-0.2485648245</x>
                                        <y>-0.0000001187</y>
                                    </vector>
                                    </point>
                                    <width>
                                    <real value="1.0000000000"/>
                                    </width>
                                    <origin>
                                    <real value="0.5000000000"/>
                                    </origin>
                                    <split>
                                    <bool value="false"/>
                                    </split>
                                    <t1>
                                    <radial_composite type="vector">
                                        <radius>
                                        <real value="0.0000000000"/>
                                        </radius>
                                        <theta>
                                        <angle value="0.000000"/>
                                        </theta>
                                    </radial_composite>
                                    </t1>
                                    <t2>
                                    <radial_composite type="vector">
                                        <radius>
                                        <real value="0.0000000000"/>
                                        </radius>
                                        <theta>
                                        <angle value="0.000000"/>
                                        </theta>
                                    </radial_composite>
                                    </t2>
                                    <split_radius>
                                    <bool value="true"/>
                                    </split_radius>
                                    <split_angle>
                                    <bool value="false"/>
                                    </split_angle>
                                </composite>
                                </entry>
                                <entry>
                                <composite guid="BEB92C43C03983CC4A7DF36D8FFE109A" type="bline_point">
                                    <point>
                                    <vector>
                                        <x>0.0000001685</x>
                                        <y>-0.4305270314</y>
                                    </vector>
                                    </point>
                                    <width>
                                    <real value="1.0000000000"/>
                                    </width>
                                    <origin>
                                    <real value="0.5000000000"/>
                                    </origin>
                                    <split>
                                    <bool value="false"/>
                                    </split>
                                    <t1>
                                    <radial_composite type="vector">
                                        <radius>
                                        <real value="0.0000000000"/>
                                        </radius>
                                        <theta>
                                        <angle value="-0.000000"/>
                                        </theta>
                                    </radial_composite>
                                    </t1>
                                    <t2>
                                    <radial_composite type="vector">
                                        <radius>
                                        <real value="0.0000000000"/>
                                        </radius>
                                        <theta>
                                        <angle value="-0.000000"/>
                                        </theta>
                                    </radial_composite>
                                    </t2>
                                    <split_radius>
                                    <bool value="true"/>
                                    </split_radius>
                                    <split_angle>
                                    <bool value="false"/>
                                    </split_angle>
                                </composite>
                                </entry>
                                <entry>
                                <composite guid="1AD522C77A896F4382230F7154F7FECB" type="bline_point">
                                    <point>
                                    <vector>
                                        <x>0.2485648692</x>
                                        <y>-0.0000000890</y>
                                    </vector>
                                    </point>
                                    <width>
                                    <real value="1.0000000000"/>
                                    </width>
                                    <origin>
                                    <real value="0.5000000000"/>
                                    </origin>
                                    <split>
                                    <bool value="false"/>
                                    </split>
                                    <t1>
                                    <radial_composite type="vector">
                                        <radius>
                                        <real value="0.0000000000"/>
                                        </radius>
                                        <theta>
                                        <angle value="0.000000"/>
                                        </theta>
                                    </radial_composite>
                                    </t1>
                                    <t2>
                                    <radial_composite type="vector">
                                        <radius>
                                        <real value="0.0000000000"/>
                                        </radius>
                                        <theta>
                                        <angle value="0.000000"/>
                                        </theta>
                                    </radial_composite>
                                    </t2>
                                    <split_radius>
                                    <bool value="true"/>
                                    </split_radius>
                                    <split_angle>
                                    <bool value="false"/>
                                    </split_angle>
                                </composite>
                                </entry>
                                <entry>
                                <composite guid="E492C2547BE39C4AA1E1A2DB3C2D40F9" type="bline_point">
                                    <point>
                                    <vector>
                                        <x>0.4971296489</x>
                                        <y>0.4305270314</y>
                                    </vector>
                                    </point>
                                    <width>
                                    <real value="1.0000000000"/>
                                    </width>
                                    <origin>
                                    <real value="0.5000000000"/>
                                    </origin>
                                    <split>
                                    <bool value="false"/>
                                    </split>
                                    <t1>
                                    <radial_composite type="vector">
                                        <radius>
                                        <real value="0.0000000000"/>
                                        </radius>
                                        <theta>
                                        <angle value="0.000000"/>
                                        </theta>
                                    </radial_composite>
                                    </t1>
                                    <t2>
                                    <radial_composite type="vector">
                                        <radius>
                                        <real value="0.0000000000"/>
                                        </radius>
                                        <theta>
                                        <angle value="0.000000"/>
                                        </theta>
                                    </radial_composite>
                                    </t2>
                                    <split_radius>
                                    <bool value="true"/>
                                    </split_radius>
                                    <split_angle>
                                    <bool value="false"/>
                                    </split_angle>
                                </composite>
                                </entry>
                                <entry>
                                <composite guid="1CB8D031A10AF4D52A8A1B2999AB3DAE" type="bline_point">
                                    <point>
                                    <vector>
                                        <x>0.0000000102</x>
                                        <y>0.4305268228</y>
                                    </vector>
                                    </point>
                                    <width>
                                    <real value="1.0000000000"/>
                                    </width>
                                    <origin>
                                    <real value="0.5000000000"/>
                                    </origin>
                                    <split>
                                    <bool value="false"/>
                                    </split>
                                    <t1>
                                    <radial_composite type="vector">
                                        <radius>
                                        <real value="0.0000000000"/>
                                        </radius>
                                        <theta>
                                        <angle value="0.000000"/>
                                        </theta>
                                    </radial_composite>
                                    </t1>
                                    <t2>
                                    <radial_composite type="vector">
                                        <radius>
                                        <real value="0.0000000000"/>
                                        </radius>
                                        <theta>
                                        <angle value="0.000000"/>
                                        </theta>
                                    </radial_composite>
                                    </t2>
                                    <split_radius>
                                    <bool value="true"/>
                                    </split_radius>
                                    <split_angle>
                                    <bool value="false"/>
                                    </split_angle>
                                </composite>
                                </entry>
                            </bline>
                            </param>
                        </layer>
                        </canvas>
                    </param>
                    <param name="time_dilation">
                        <real value="1.0000000000"/>
                    </param>
                    <param name="time_offset">
                        <time value="0s"/>
                    </param>
                    <param name="children_lock">
                        <bool value="true"/>
                    </param>
                    <param name="outline_grow">
                        <real value="0.0000000000"/>
                    </param>
                    <param name="z_range">
                        <bool value="false" static="true"/>
                    </param>
                    <param name="z_range_position">
                        <real value="0.0000000000"/>
                    </param>
                    <param name="z_range_depth">
                        <real value="0.0000000000"/>
                    </param>
                    <param name="z_range_blur">
                        <real value="0.0000000000"/>
                    </param>
                    </layer>
                    <layer type="advanced_outline" active="true" exclude_from_rendering="false" version="0.3" desc="Limits">
                    <param name="z_depth">
                        <real value="0.0000000000"/>
                    </param>
                    <param name="amount">
                        <real value="1.0000000000"/>
                    </param>
                    <param name="blend_method">
                        <integer value="0"/>
                    </param>
                    <param name="color">
                        <color>
                        <r>0.000000</r>
                        <g>0.000000</g>
                        <b>0.000000</b>
                        <a>1.000000</a>
                        </color>
                    </param>
                    <param name="origin">
                        <vector>
                        <x>0.0000000000</x>
                        <y>0.1666666716</y>
                        </vector>
                    </param>
                    <param name="invert">
                        <bool value="false"/>
                    </param>
                    <param name="antialias">
                        <bool value="true"/>
                    </param>
                    <param name="feather">
                        <real value="0.0000000000"/>
                    </param>
                    <param name="blurtype">
                        <integer value="1"/>
                    </param>
                    <param name="winding_style">
                        <integer value="0"/>
                    </param>
                    <param name="bline">
                        <bline guid="C19377D913E5ECE93151ED9E27B58259" type="bline_point">
                        <entry>
                            <composite guid="4BD115A9C2E2CA2D73C510FDD5B029E7" type="bline_point">
                            <point>
                                <vector>
                                <x>-1.6666667461</x>
                                <y>0.0833333358</y>
                                </vector>
                            </point>
                            <width>
                                <real value="1.0000000000"/>
                            </width>
                            <origin>
                                <real value="0.5000000000"/>
                            </origin>
                            <split>
                                <bool value="false"/>
                            </split>
                            <t1>
                                <radial_composite type="vector">
                                <radius>
                                    <real value="0.0000000000"/>
                                </radius>
                                <theta>
                                    <angle value="0.000000"/>
                                </theta>
                                </radial_composite>
                            </t1>
                            <t2>
                                <radial_composite type="vector">
                                <radius>
                                    <real value="0.0000000000"/>
                                </radius>
                                <theta>
                                    <angle value="180.000000"/>
                                </theta>
                                </radial_composite>
                            </t2>
                            <split_radius>
                                <bool value="true"/>
                            </split_radius>
                            <split_angle>
                                <bool value="false"/>
                            </split_angle>
                            </composite>
                        </entry>
                        <entry>
                            <composite guid="11FEE7C15F29985125A914EB159B9D49" type="bline_point">
                            <point>
                                <vector>
                                <x>-1.6666666269</x>
                                <y>-0.1666666716</y>
                                </vector>
                            </point>
                            <width>
                                <real value="1.0000000000"/>
                            </width>
                            <origin>
                                <real value="0.0735090971"/>
                            </origin>
                            <split>
                                <bool value="false"/>
                            </split>
                            <t1>
                                <radial_composite type="vector">
                                <radius>
                                    <real value="0.0000000000"/>
                                </radius>
                                <theta>
                                    <angle value="-0.000000"/>
                                </theta>
                                </radial_composite>
                            </t1>
                            <t2>
                                <radial_composite type="vector">
                                <radius>
                                    <real value="0.0000000000"/>
                                </radius>
                                <theta>
                                    <angle value="-0.000000"/>
                                </theta>
                                </radial_composite>
                            </t2>
                            <split_radius>
                                <bool value="true"/>
                            </split_radius>
                            <split_angle>
                                <bool value="false"/>
                            </split_angle>
                            </composite>
                        </entry>
                        <entry>
                            <composite guid="FA2CB23F728416598284FFF9058C403F" type="bline_point">
                            <point>
                                <vector>
                                <x>1.6666666269</x>
                                <y>-0.1666666716</y>
                                </vector>
                            </point>
                            <width>
                                <real value="1.0000000000"/>
                            </width>
                            <origin>
                                <real value="0.9143519402"/>
                            </origin>
                            <split>
                                <bool value="false"/>
                            </split>
                            <t1>
                                <radial_composite type="vector">
                                <radius>
                                    <real value="0.0000000000"/>
                                </radius>
                                <theta>
                                    <angle value="-0.000000"/>
                                </theta>
                                </radial_composite>
                            </t1>
                            <t2>
                                <radial_composite type="vector">
                                <radius>
                                    <real value="0.0000000000"/>
                                </radius>
                                <theta>
                                    <angle value="-0.000000"/>
                                </theta>
                                </radial_composite>
                            </t2>
                            <split_radius>
                                <bool value="true"/>
                            </split_radius>
                            <split_angle>
                                <bool value="false"/>
                            </split_angle>
                            </composite>
                        </entry>
                        <entry>
                            <composite guid="0F5A0FE11CC375D5273BF91F5BA8D5BC" type="bline_point">
                            <point>
                                <vector>
                                <x>1.6666667461</x>
                                <y>0.0833333358</y>
                                </vector>
                            </point>
                            <width>
                                <real value="1.0000000000"/>
                            </width>
                            <origin>
                                <real value="0.5000000000"/>
                            </origin>
                            <split>
                                <bool value="false"/>
                            </split>
                            <t1>
                                <radial_composite type="vector">
                                <radius>
                                    <real value="0.0000000000"/>
                                </radius>
                                <theta>
                                    <angle value="0.000000"/>
                                </theta>
                                </radial_composite>
                            </t1>
                            <t2>
                                <radial_composite type="vector">
                                <radius>
                                    <real value="0.0000000000"/>
                                </radius>
                                <theta>
                                    <angle value="0.000000"/>
                                </theta>
                                </radial_composite>
                            </t2>
                            <split_radius>
                                <bool value="true"/>
                            </split_radius>
                            <split_angle>
                                <bool value="false"/>
                            </split_angle>
                            </composite>
                        </entry>
                        </bline>
                    </param>
                    <param name="width">
                        <real value="0.1666666719"/>
                    </param>
                    <param name="expand">
                        <real value="0.0000000000"/>
                    </param>
                    <param name="start_tip">
                        <integer value="1"/>
                    </param>
                    <param name="end_tip">
                        <integer value="1"/>
                    </param>
                    <param name="cusp_type">
                        <integer value="1"/>
                    </param>
                    <param name="smoothness">
                        <real value="1.0000000000"/>
                    </param>
                    <param name="homogeneous">
                        <bool value="true" static="true"/>
                    </param>
                    <param name="wplist">
                        <wplist type="width_point">
                        <entry>
                            <composite guid="930E9A57618A34B52050FD075CB4A4FA" type="width_point">
                            <position>
                                <real value="0.1000000000"/>
                            </position>
                            <width>
                                <real value="1.0000000000"/>
                            </width>
                            <side_before>
                                <integer value="0"/>
                            </side_before>
                            <side_after>
                                <integer value="0"/>
                            </side_after>
                            <lower_bound>
                                <real value="0.0000000000" static="true"/>
                            </lower_bound>
                            <upper_bound>
                                <real value="1.0000000000" static="true"/>
                            </upper_bound>
                            </composite>
                        </entry>
                        <entry>
                            <composite guid="F19F5B6B3033C1666EEBFAC91276FB6A" type="width_point">
                            <position>
                                <real value="0.9000000000"/>
                            </position>
                            <width>
                                <real value="1.0000000000"/>
                            </width>
                            <side_before>
                                <integer value="0"/>
                            </side_before>
                            <side_after>
                                <integer value="0"/>
                            </side_after>
                            <lower_bound>
                                <real value="0.0000000000" static="true"/>
                            </lower_bound>
                            <upper_bound>
                                <real value="1.0000000000" static="true"/>
                            </upper_bound>
                            </composite>
                        </entry>
                        </wplist>
                    </param>
                    <param name="dash_enabled">
                        <bool value="false"/>
                    </param>
                    <param name="dilist">
                        <dilist type="dash_item">
                        <entry>
                            <composite guid="2186D8210E86B568C60AFAD4B30DF6F9" type="dash_item">
                            <offset>
                                <real value="0.1000000000"/>
                            </offset>
                            <length>
                                <real value="0.1000000000"/>
                            </length>
                            <side_before>
                                <integer value="4"/>
                            </side_before>
                            <side_after>
                                <integer value="4"/>
                            </side_after>
                            </composite>
                        </entry>
                        </dilist>
                    </param>
                    <param name="dash_offset">
                        <real value="0.0000000000"/>
                    </param>
                    </layer>
                </canvas>
                </param>
                <param name="time_dilation">
                <real value="1.0000000000"/>
                </param>
                <param name="time_offset">
                <time value="0s"/>
                </param>
                <param name="children_lock">
                <bool value="false"/>
                </param>
                <param name="outline_grow">
                <real value="0.0000000000"/>
                </param>
                <param name="z_range">
                <bool value="false" static="true"/>
                </param>
                <param name="z_range_position">
                <real value="0.0000000000"/>
                </param>
                <param name="z_range_depth">
                <real value="0.0000000000"/>
                </param>
                <param name="z_range_blur">
                <real value="0.0000000000"/>
                </param>
            </layer>
        ''')
    root.append(sliderUI)
