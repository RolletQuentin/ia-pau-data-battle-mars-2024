import { ColorRect, MarginContainer, Text } from "@liro_u/react-components";
import React from "react";

const Tableau = ({
  tab,
  color,
  titleFontWeight,
  titleFontSize,
  subSectionFontSize = "15",
  border = "solid 0px var(--dark-primary)",
  marginCase = "10px",
  headerBackgroundColor = "var(--dark-primary)",
  evenBackgroundColor = "var(--primary-pastel)",
  oddBackgroundColor = "var(--dark-primary-pastel)",
  headerTextBackgroundColor = "var(--light-color)",
}) => {
  return (
    <table style={{ border, borderCollapse: "collapse" }}>
      {tab.map((line, index1) => {
        return (
          <tr key={index1} style={{ border, borderCollapse: "collapse" }}>
            {line.map((col, index2) => {
              return (
                <td key={index2} style={{ border, borderCollapse: "collapse" }}>
                  <ColorRect
                    backgroundColor={
                      index1 % 2 === 0
                        ? evenBackgroundColor
                        : oddBackgroundColor
                    }
                  >
                    <MarginContainer margin={marginCase}>
                      <Text
                        text={col}
                        fontSize={subSectionFontSize + "px"}
                        color={color}
                      />
                    </MarginContainer>
                  </ColorRect>
                </td>
              );
            })}
          </tr>
        );
      })}
    </table>
  );
};

export default Tableau;
