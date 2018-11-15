class XMLDefinitions:
    shippingContainerXML = """
        <ScaleEvent id="a91b81dd-f2d0-4ab1-90f1-42faa9d1f9bc" generatedAt="2018-11-14T10:03:23" source="2017">
            <ShippingContainer id="00000000000527072333">
                <PickingWave>
                    <Name>3B West</Name>
                    <LaunchNo>67</LaunchNo>
                </PickingWave>
                <Shipment>
                    <ShipmentId>3IOWK1QIAHNQGDB4-1</ShipmentId>
                    <Route>C01A</Route>
                    <ShippingBatch>102</ShippingBatch>
                    <Zone>Central</Zone>
                </Shipment>
                <Order>
                    <ErpOrderNumber>512190933</ErpOrderNumber>
                </Order>
                <Priority>6</Priority>
                <CaseType>SplitCase</CaseType>
                <ContainerType>IP</ContainerType>
                <Chamber>Dry</Chamber>
                <QcStatus>true</QcStatus>
                <WorkUnit instructionCount="1">
                </WorkUnit>
            </ShippingContainer>
        </ScaleEvent>"""

    workInstructionXML = """ <WorkInstruction id="431074366">
                    <Item>23342</Item>
                    <UOM>EA</UOM>
                    <Quantity>5</Quantity>
                    <Lot>60706457</Lot>
                    <Location>WNL-A-034-B-04</Location>
                    <WorkZone>Work 25C Bulk Pick</WorkZone>
                    <PickInstruction>Handle with utmost care</PickInstruction>
                    <ErpOrderLineNum>1</ErpOrderLineNum>
                    <InternalContainerNum>1294739</InternalContainerNum>
                    <CatchWeightReqd>N</CatchWeightReqd>
                </WorkInstruction>"""
