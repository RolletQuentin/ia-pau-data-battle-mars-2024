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
  solution,
}) => {
  return (
    <MarginContainer margin={margin}>
      <HBox gap={gap}>
        <Text
          text={solution.num}
          color={textColor}
          fontSize={fontSize}
          fontWeight={fontWeight}
          style={{
            width: "calc(" + percentageSplit[0] + "% - " + gap + ")",
            textAlign: "left",
          }}
        />
        <Text
          text={solution.titre}
          color={textColor}
          fontSize={fontSize}
          fontWeight={fontWeight}
          style={{
            width: "calc(" + percentageSplit[1] + "% - " + gap + ")",
            textAlign: "left",
          }}
        />
        <Text
          text={"Basé sur " + solution.degre_confiance + " études"}
          color={textColor}
          fontSize={fontSize}
          fontWeight={fontWeight}
          style={{
            width: "calc(" + percentageSplit[2] + "% - " + gap + ")",
            textAlign: "left",
          }}
        />
        <Text
          text={solution.gain_monetaire + " €/an"}
          color={textColor}
          fontSize={fontSize}
          fontWeight={fontWeight}
          style={{
            width: "calc(" + percentageSplit[3] + "% - " + gap + ")",
            textAlign: "left",
          }}
        />
        <Text
          text={solution.gain_watt + " GWh/an"}
          color={textColor}
          fontSize={fontSize}
          fontWeight={fontWeight}
          style={{
            width: "calc(" + percentageSplit[4] + "% - " + gap + ")",
            textAlign: "left",
          }}
        />
        <Text
          text={solution.gain_co2 + "T"}
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
