import { CenterContainer, MarginContainer } from "@liro_u/react-components";
import React from "react";
import SolutionDetails from "./SolutionDetails";

const CustomScrollbar = () => {
  return (
    <MarginContainer margin="30px" style={{ height: "90vh" }}>
      <CenterContainer>
        <SolutionDetails />
      </CenterContainer>
    </MarginContainer>
  );
};

export default CustomScrollbar;
