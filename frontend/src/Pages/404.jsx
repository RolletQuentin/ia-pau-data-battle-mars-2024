import { CenterContainer, Text, VBox } from "@liro_u/react-components";
import React from "react";

const Page404 = () => {
  return (
    <CenterContainer>
      <VBox>
        <CenterContainer>
          <Text text="404" fontSize="50px" fontWeight="bold" />
        </CenterContainer>
        <CenterContainer>
          <Text text="Page not found" />
        </CenterContainer>
      </VBox>
    </CenterContainer>
  );
};

export default Page404;
