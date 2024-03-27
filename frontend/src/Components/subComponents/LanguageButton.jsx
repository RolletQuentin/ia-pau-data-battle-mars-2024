import { useState } from "react";
import i18n, { changeLanguage } from "../../i18n";
import { useTranslation } from "react-i18next";
import { HBox, Text } from "@liro_u/react-components";

const LanguageButton = ({ lg }) => {
  const { t } = useTranslation();

  const [isHover, setIsHover] = useState(false);

  const handleHover = (hoverBool) => {
    setIsHover(hoverBool);
  };

  return (
    <HBox
      gap="10px"
      onClick={() => {
        console.log("change to " + lg);
        changeLanguage(lg);
      }}
      style={{ cursor: "pointer" }}
      onMouseEnter={() => handleHover(true)}
      onMouseLeave={() => handleHover(false)}
    >
      <span
        style={{
          border: "4px solid",
          borderColor: isHover || lg === i18n.language ? "#fff" : "#fff0",
          borderRadius: "30px",
          height: 0,
          margin: "auto 0",
        }}
      />
      <Text
        fontSize="15px"
        text={t("language." + lg)}
        color={isHover || lg === i18n.language ? "#fff" : "#555"}
      />
    </HBox>
  );
};

export default LanguageButton;
