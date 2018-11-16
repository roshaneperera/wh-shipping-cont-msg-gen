class XMLDefinitions:
    shippingContainerSOPTXML = """
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

    shippingContainerMOPTXML = """
    <ScaleEvent id="8559c90a-13dc-4fc6-b2f0-e8a9e5a21415" generatedAt="2018-11-15T13:45:03" source="2017">
    <ShippingContainer id="00000000000537286092">
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
            <ErpOrderNumber>540519473</ErpOrderNumber>
        </Order>
        <Priority>6</Priority>
        <CaseType>SplitCase</CaseType>
        <ContainerType>MOPT_FRZ_11</ContainerType>
        <Chamber>Frozen</Chamber>
        <QcStatus>true</QcStatus>
        <MoptGroupId>0</MoptGroupId>
        <WorkUnit instructionCount="3"> 
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
