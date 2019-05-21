# Licensed under a 3-clause BSD style license - see LICENSE.rst

from astropy.coordinates import SkyCoord
import astropy.units as u
import numpy as np
from numpy.testing import assert_array_equal


class BaseTestApertureParams:
    index = 2
    slc = slice(0, 2)
    expected_slc_len = 2


class BaseTestAperture(BaseTestApertureParams):
    def test_index(self):
        aper = self.aperture[self.index]
        assert isinstance(aper, self.aperture.__class__)
        assert aper.isscalar
        expected_positions = self.aperture.positions[self.index]
        if isinstance(expected_positions, SkyCoord):
            assert u.allclose(aper.positions.ra, expected_positions.ra)
            assert u.allclose(aper.positions.dec, expected_positions.dec)
        else:
            assert_array_equal(aper.positions, expected_positions)
            for param in aper._params:
                assert getattr(aper, param) == getattr(self.aperture, param)

    def test_slice(self):
        aper = self.aperture[self.slc]
        assert isinstance(aper, self.aperture.__class__)
        assert len(aper) == self.expected_slc_len

        expected_positions = self.aperture.positions[self.slc]
        if isinstance(self.aperture.positions, SkyCoord):
            assert u.allclose(aper.positions.ra, expected_positions.ra)
            assert u.allclose(aper.positions.dec, expected_positions.dec)
        else:
            assert_array_equal(aper.positions, expected_positions)
            for param in aper._params:
                assert getattr(aper, param) == getattr(self.aperture, param)
