import { HBox, MarginContainer, Text } from "@liro_u/react-components";
import React from "react";
import CustomButton from "./input/CustomButton";

const SubSolutionDisplay = ({
  textColor = "var(--dark-primary)",
  margin = "20px",
  fontSize = 15,
  fontWeight = "bold",
  gap = "20px",
  percentageSplit = [10, 30, 20, 10, 10, 10, 10],
}) => {
  return (
    <MarginContainer margin={margin}>
      <HBox gap={gap}>
        <Text
          text="1686"
          color={textColor}
          fontSize={fontSize}
          fontWeight={fontWeight}
          style={{
            width: "calc(" + percentageSplit[0] + "% - " + gap + ")",
            textAlign: "left",
          }}
        />
        <Text
          text="Optimisation contrat eau / Taxes d'assainissement"
          color={textColor}
          fontSize={fontSize}
          fontWeight={fontWeight}
          style={{
            width: "calc(" + percentageSplit[1] + "% - " + gap + ")",
            textAlign: "left",
          }}
        />
        <Text
          text="Basé sur 15 études"
          color={textColor}
          fontSize={fontSize}
          fontWeight={fontWeight}
          style={{
            width: "calc(" + percentageSplit[2] + "% - " + gap + ")",
            textAlign: "left",
          }}
        />
        <Text
          text="1 832 066 €/an"
          color={textColor}
          fontSize={fontSize}
          fontWeight={fontWeight}
          style={{
            width: "calc(" + percentageSplit[3] + "% - " + gap + ")",
            textAlign: "left",
          }}
        />
        <Text
          text="53 GWh/an"
          color={textColor}
          fontSize={fontSize}
          fontWeight={fontWeight}
          style={{
            width: "calc(" + percentageSplit[4] + "% - " + gap + ")",
            textAlign: "left",
          }}
        />
        <Text
          text="100T"
          color={textColor}
          fontSize={fontSize}
          fontWeight={fontWeight}
          style={{
            width: "calc(" + percentageSplit[5] + "% - " + gap + ")",
            textAlign: "left",
          }}
        />
        <CustomButton
          buttonWidth={"calc(" + percentageSplit[6] + "% - " + gap + ")"}
          text="Détails"
        />
      </HBox>
    </MarginContainer>
  );
};

export default SubSolutionDisplay;
